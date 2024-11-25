# Adding callback
from datetime import datetime
import asyncio


async def say(msg, *, delay):
    print(f"Started {datetime.now():%H:%M:%S}")
    await asyncio.sleep(delay=delay)
    print(msg)
    print(f"Ended {datetime.now():%H:%M:%S}")
    return f'Returned - {msg}'

async def task():
    taskset = set() # set to track the number of tasks
    task1 = asyncio.create_task(say('lol',delay=5))
    task2 = asyncio.create_task(say('lol2',delay=10))
    taskset.add(task1)
    taskset.add(task2)
    print(f'Number of tasks: {len(taskset)}')
    task1.add_done_callback(taskset.discard) # once the task is done the callback function is called.
    task2.add_done_callback(taskset.discard)
    await task1
    print(f'Number of pending tasks: {len(taskset)}')
    print(f'{task1.done()=}')
    await task2
    print(f'Number of pending tasks: {len(taskset)}')
    print(f'{task2.done()=}')

asyncio.run(task())
