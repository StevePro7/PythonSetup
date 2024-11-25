# Synchronization Primitives
from datetime import datetime
import time
import asyncio

lock = asyncio.Lock()

async def say(msg, *, delay):
    # lock the resource. only one coroutine can access this block at a given time
    async with lock:
        print(f"Started {datetime.now():%H:%M:%S}")
        await asyncio.sleep(delay=delay)
        print(msg)
        print(f"Ended {datetime.now():%H:%M:%S}")
        return f'Returned - {msg}'

async def simple_task():
    task1 = asyncio.create_task(say('Task1 lol',delay=4))
    task2 = asyncio.create_task(say('Task2 lol',delay=2))
    r1 = await task1
    print(r1)
    r2 = await task2
    print(r2)

start = time.perf_counter()
asyncio.run(simple_task())
end = time.perf_counter()
print(f'Total execution time: {end-start}s')