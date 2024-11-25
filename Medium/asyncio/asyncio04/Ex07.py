# Timeout handling
from datetime import datetime
import asyncio

async def say(msg, *, delay):
    print(f"Started {datetime.now():%H:%M:%S}")
    await asyncio.sleep(delay=delay)
    print(msg)
    print(f"Ended {datetime.now():%H:%M:%S}")
    return f'Returned - {msg}'

async def task():
    task1 = asyncio.create_task(say('lol',delay=5))
    try:
        result = await asyncio.wait_for(task1, 2)
        # this will raise the timeout error since we haven't provided enough time to complete the task
    except asyncio.TimeoutError as te:
        print('Timeout error occurs')

asyncio.run(task())