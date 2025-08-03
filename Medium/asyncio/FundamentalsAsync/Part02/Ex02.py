import asyncio
import random


async def producer(queue, producer_id):
    """Produces work items and puts them in the queue"""
    for i in range(3):
        item = f"Item-{producer_id}-{i}"
        await queue.put(item)
        print(f"Producer {producer_id} created {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))


async def consumer(queue, consumer_id):
    """Consumes work items from the queue"""
    while True:
        try:
            # Wait for work, but timeout after 2 seconds
            item = await asyncio.wait_for(queue.get(), timeout=2.0)
            print(f"Consumer {consumer_id} processing {item}")
            await asyncio.sleep(random.uniform(0.2, 0.8))  # Simulate processing
            queue.task_done()  # Mark task as completed
        except asyncio.TimeoutError:
            print(f"Consumer {consumer_id} timed out, shutting down")
            break


async def demo_queue():
    queue = asyncio.Queue(maxsize=5)  # Limit queue size

    # Start producers and consumers
    producers = [producer(queue, i) for i in range(2)]
    consumers = [consumer(queue, i) for i in range(3)]

    # Run everything concurrently
    await asyncio.gather(*producers, *consumers)


asyncio.run(demo_queue())