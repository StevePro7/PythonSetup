# Run many awaitables as group
from datetime import datetime
import time
import asyncio

async def say(msg, *, delay): # coroutine
    print(f"Started {datetime.now():%H:%M:%S}")
    await asyncio.sleep(delay=delay)
    print(msg)
    print(f"Ended {datetime.now():%H:%M:%S}")
    return f'Returned - {msg}'

async def gather():
    # Schedule tasks concurrently. Event loop
    gather_list = asyncio.gather(
        say('gather lol', delay=2),
        say('gather lol2', delay=4),
    )
    out_list = await gather_list
    print(gather_list) # object
    print(out_list) # results

start = time.perf_counter()
asyncio.run(gather())
end = time.perf_counter()
print(f'Total execution time: {end-start}s')