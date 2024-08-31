Mastering Python’s Asyncio: A Practical Guide
29-Aug-2024

https://medium.com/@moraneus/mastering-pythons-asyncio-a-practical-guide-0a673265cf04


Event Loop
manage + distribute execution of different tasks in async.io
handles events + schedules async routines


Coroutines
async functions declared
async def
I/O ops run in background


Futures
objects represent result of work not yet completed
returned form tasks scheduled by the event loop


Tasks
scheduled coroutines wrapped in future object by event loop


AWAIT
used to pause execution of async function until awaitable object
[coroutine, task, future, I/O] completes
allows other tasks to run in the meantime
enabled efficient I/O bound tasks + network code


Context
await only used in async functions

Purpose
yield control back to the event loop
suspend execution of enclosing coroutine untile awaited object resolved
non-blocking behavior makes asynchronous programming efficient
esp. I/O-bound tasks

Awaitables
any object with __await__() method
e.g.
async def
but include asycio Tasks, Futures etc.


IMPORTANT
asyncio.gather()
execute multiple functions concurrently


Fetching Web Pages (Concurrent I/O Tasks)
aiohttp
could not install on Windows


Reading Files (Concurrent I/O Tasks)
pip install aiofiles
could not install on Windows


Mixing Async and Sync: A Hybrid Approach
uses:
integration with legacy code
working with blocking I/O
i.e. blocking network or file read/write [I/O] calls
CPU bound tasks


The Future() Object


SUMMARY
asyncio
improve performance + scalability of I/O bound + network-driven programs

event loops, coroutines, futures, tasks
Devs write efficient non-blocking code to handle
simultaneous connections

asyncio EX
achieve concurrency in Python apps