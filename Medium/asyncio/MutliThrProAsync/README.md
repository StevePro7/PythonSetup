Unlocking Python’s Power: Multithreading, Multiprocessing, and Async Programming
04-Nov-2024

Reference:
https://medium.com/@nomannayeem/unlocking-pythons-power-multithreading-multiprocessing-and-async-programming-d659d3c75fa7

Multithreading
multiple threads in same process
ideal for I/O bound tasks - program spends lot of time waiting for external resources
file ops
data ops
network requests


Multiprocessing
multiple CPU cores run by separate processes
GIL sidestepped - ideal for CPU bound tasks - tasks = heavy computation


Async programming
asyncio module
designed for high-level I/O bound and structured network code
ideal for I/O bound code that involves a lot of waiting e.g. network requests
concurrent code - async / await
handle thousands of network connections at once


Multithreading
threading module
start()
join()				wait for thread to finish
daemon [background] threads


Multiprocessing
multiprocessing module
ProcessPoolExecutor from concurrent.futures module - manage pool of worker processes
submit()			task submitted to pool
result()			result from processes from Future objects


Async programming
does not create additional threads or processes BUT
uses a single thread to manage multiple tasks - switches between them
as they await completion of I/O operations

Coroutines			functions defined async def paused/resumed using await
Event Loop			managed execution of asynchronous tasks
Tasks				created via asyncio.create_task()
Async Context Mgr	used to manage asynchronous resources


USE CASES
Multithreading		File Reading and Network Calls
Multiprocessing		Batch Image Processing
Async programming	Web Server Handling Multiple Requests


TIPS
Multithreading
Minimize shared state
Use locks
Daemon threads
Avoid blocking calls


Multiprocessing
Use queues for communication
Manage resourcesa
Avoid forking in threads
Pickleable objects


Async programming
Use async/await correctly
Limit concurrency
Graceful shutdown
Handle exceptions


PITFALLS
Deadlocks
Avoid: ensure that all locks are acquired and released in a consistent order

Race conditions
multiple threads / processes access shared resources simultaneously
Avoid: use locks, semaphores, or queues to manage shared resource access

Resource leaks
Avoid: use Context Managers [with] to release resources e.g.
file handles, database connections, and network sockets

Blocking the Event loop
Avoid blocking event loop w/ synchronous calls
Avoid: use await to yield control back to event loop


SUMMARY
Multithreading			concurrent network requests
I/O bound tasks waiting for external resources e.g.
file I/O or network operations

Multiprocessing			Data processing
CPU bound tasks
leverage multiple CPU cores for computationslly intensive tasks

Async programming		Web scraping
I/O bound tasks w/ lot of time waiting
thousands of network connections or asynchronous file operations


FINALLY
Minimize shared state in multithreading
Use locks when necessary
Use queues for communication btwn processes [multiprocessing]
Handle exceptions
Manage resources in async programming - avoid blocking event loop