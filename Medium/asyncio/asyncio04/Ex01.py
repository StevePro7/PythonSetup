# What is Coroutine?
from datetime import datetime
import time
import asyncio

async def say(msg, *, delay): # coroutine
    print(f"Started {datetime.now():%H:%M:%S}")
    await asyncio.sleep(delay=delay)
    print(msg)
    print(f"Ended {datetime.now():%H:%M:%S}")
    return f'Returned - {msg}'

start = time.perf_counter()
r1 = asyncio.run(say('Logesh', delay=2)) # Run the coroutine and returns result
print(r1)
r2 = asyncio.run(say('Sakthivel', delay=4))
print(r2)
end = time.perf_counter()
print(f'Total execution time: {end-start}s')