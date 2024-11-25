# Cancel task
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
    await asyncio.sleep(2)
    task1.cancel('Took too long...') # cancel the task with message
    try:
        print('Waiting for the task after cancel')
        await task1
    except asyncio.CancelledError as ce:
        print('Exception occured')
        print(ce)
    print(f'{task1.cancelled()=}') # we can also check whether the task is cancelled

asyncio.run(task())
