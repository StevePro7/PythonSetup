import asyncio

counter = 0
counter_lock = asyncio.Lock()

async def increment_counter(worker_id):
    global counter

    for i in range(3):
        async with counter_lock:
            current = counter
            await asyncio.sleep(0.1)
            counter = current + 1
            print(f"Worke {worker_id}: counter = {counter}")

async def demo_lock():
    # Start multiple workers that all increment the same counter
    workers = [increment_counter(i) for i in range(3)]
    await asyncio.gather(*workers)
    print(f"Final counter value: {counter}")

asyncio.run(demo_lock())