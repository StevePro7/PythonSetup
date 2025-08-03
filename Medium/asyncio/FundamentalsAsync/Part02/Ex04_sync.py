import asyncio
import concurrent.futures
import requests             # Synchronous library
import time

def sync_http_call(url):
    """A blocking HTTP call using requests library"""
    response = requests.get(url)
    return {
        'url': url,
        'status': response.status_code,
        'length': len(response.content)
    }

async def async_http_calls(urls):
    """Run sync HTTP calls in a thread pool"""
    loop = asyncio.get_event_loop()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all sync operations to the thread pool
        futures = [
            loop.run_in_executor(executor, sync_http_call, url)
            for url in urls
        ]

        # WAit for all to complete
        results = await asyncio.gather(*futures)
        return results

async def mixed_sync_async():
    """Demo mix sync and async operations"""
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/status/200'
    ]

    start = time.time()

    # These sync operations run concurrently in threads
    http_results = await async_http_calls(urls)

    # This i snative async
    await asyncio.sleep(0.5)

    print(f"Completed in {time.time() - start:.2f}")
    return http_results

# Run the mixed example
results = asyncio.run(mixed_sync_async())
for result in results:
    print(f"URL: {result['url']}, Status: {result['status']}")
