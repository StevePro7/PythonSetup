import asyncio
import logging
from dataclasses import dataclass
from typing import List, Optional
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ProcessingResult:
    item_id: str
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None


class AsyncDataProcessor:
    """Main application class demonstrating async architecture"""

    def __init__(self, max_concurrent_requests: int = 5):
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.session: Optional[aiohttp.ClientSession] = None
        self.results_queue = asyncio.Queue()

    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup resources"""
        if self.session:
            await self.session.close()

    async def fetch_data(self, item_id: str) -> ProcessingResult:
        """Fetch data for a single item with rate limiting"""
        async with self.semaphore:
            try:
                url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"

                async with self.session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        logger.info(f"Successfully fetched item {item_id}")
                        return ProcessingResult(item_id, True, data)
                    else:
                        error_msg = f"HTTP {response.status}"
                        logger.error(f"Failed to fetch item {item_id}: {error_msg}")
                        return ProcessingResult(item_id, False, error=error_msg)

            except Exception as e:
                error_msg = str(e)
                logger.error(f"Exception fetching item {item_id}: {error_msg}")
                return ProcessingResult(item_id, False, error=error_msg)

    async def process_item(self, result: ProcessingResult) -> ProcessingResult:
        """Process fetched data"""
        if not result.success:
            return result

        try:
            # Simulate processing time
            await asyncio.sleep(0.1)

            # Example processing: extract title length
            processed_data = {
                'original_title': result.data.get('title', ''),
                'title_length': len(result.data.get('title', '')),
                'word_count': len(result.data.get('body', '').split()),
                'processed_at': asyncio.get_event_loop().time()
            }

            result.data = processed_data
            logger.info(f"Processed item {result.item_id}")
            return result

        except Exception as e:
            error_msg = f"Processing error: {str(e)}"
            logger.error(f"Failed to process item {result.item_id}: {error_msg}")
            return ProcessingResult(result.item_id, False, error=error_msg)

    async def worker(self, item_ids: List[str]):
        """Worker that fetches and processes items"""
        for item_id in item_ids:
            # Fetch data
            fetch_result = await self.fetch_data(item_id)

            # Process data
            processed_result = await self.process_item(fetch_result)

            # Store result
            await self.results_queue.put(processed_result)

    async def result_collector(self, expected_count: int) -> List[ProcessingResult]:
        """Collect results as they become available"""
        results = []

        while len(results) < expected_count:
            try:
                result = await asyncio.wait_for(
                    self.results_queue.get(),
                    timeout=30.0
                )
                results.append(result)
                logger.info(f"Collected result {len(results)}/{expected_count}")

            except asyncio.TimeoutError:
                logger.error("Timeout waiting for results")
                break

        return results

    async def process_batch(self, item_ids: List[str],
                            batch_size: int = 10) -> List[ProcessingResult]:
        """Process items in batches with concurrent workers and result collection"""

        # Split items into batches
        batches = [
            item_ids[i:i + batch_size]
            for i in range(0, len(item_ids), batch_size)
        ]

        # Start result collector
        collector_task = asyncio.create_task(
            self.result_collector(len(item_ids))
        )

        # Start worker tasks for each batch
        worker_tasks = [
            asyncio.create_task(self.worker(batch))
            for batch in batches
        ]

        # Wait for all workers to complete
        await asyncio.gather(*worker_tasks)

        # Get collected results
        results = await collector_task

        return results


async def main():
    """Main application entry point"""
    # Items to process
    item_ids = [str(i) for i in range(1, 21)]  # Process items 1-20

    async with AsyncDataProcessor(max_concurrent_requests=3) as processor:
        logger.info(f"Starting processing of {len(item_ids)} items")

        start_time = asyncio.get_event_loop().time()
        results = await processor.process_batch(item_ids, batch_size=5)
        end_time = asyncio.get_event_loop().time()

        # Analyse results
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]

        print("\n=== Processing Complete ===")
        print(f"Total time: {end_time - start_time:.2f}s")
        print(f"Successful: {len(successful)}/{len(results)}")
        print(f"Failed: {len(failed)}/{len(results)}")

        if failed:
            print("\nFailures:")
            for failure in failed:
                print(f"  {failure.item_id}: {failure.error}")

        if successful:
            print("\nSample successful result:")
            sample = successful[0]
            print(f"  Item {sample.item_id}: {sample.data}")


if __name__ == "__main__":
    asyncio.run(main())