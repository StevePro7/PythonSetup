Asynchronous Programming in Python: A Deep Dive
18-oCT-2024


Asychronous programming
capable of handling multiple tasks concurrently
without waiting for each task to complete before moving onto next one

asynchronous programming allows for tasks to be paused and resumed
optimizing resource usage and improving overall performance

asyncio
async / await
useful where tasks involve I/O operations
e.g.
- network requests
- file I/O
- database queries

i.e.
tasks that would block execution of other tasks


Asynchronous programming
allows program to continue executing other tasks while waiting for
I/O operations to complete

leads to better resource utilization, reduced latency and ability to
handle more tasks simultaneously


CONCEPTS
1. Coroutines
special functions defined using
async def
   
paused and resumed using
await


2. Event Loop
engine that drives asynchronous programming
managed execution of coroutines
schedules coroutines ans switches btwn them when they yield control
   

3. Tasks and Futures
task    = coroutine scheduled for execution
tasks are used to run coroutines concurrently
   
future  = result of an asynchronous operation
tracks progress of task and retrieves result once completed


4. Non-blocking I/O
program can continue executing other tasks while waiting
for the I/O operation to complete
   

5. Concurrency vs. Parallelism
Concurrency     multiple tasks making progress at the same time
Parallelism     tasks running simultaneously on multiple CPU cores
   

IMPORTANT
Asynchronous programming deals with concurrency
allowing a single-threaded program to handle multiple tasks efficiently


EXAMPLE
pip install aiohttp


Concurrent requests
asynchronous coroutine that makes HTTP GET request
await function call yields control back to the event loop
this allows other coroutines to run while waiting for response


Efficient Execution
each coroutine fetches data
tasks scheduled to run concurrently using
asyncio.gather()

can make multiple requests in parallel
reducing time needed to fetch data


Resource Utilization
event loop efficiently manages execution of these tasks
ensuring that the program doesn't waste time waiting idly
for I/O operations to complete


CONCLUSION
Asynchronous programming in Python offers way to handle tasks that
involve waiting for external events like I/O operations

asyncio
coroutines
event loops
tasks
futures

write code that is more responsive and can handle higher loads
with fewer resources