How to Use Coroutines in Python: A Beginner Guide
17-Apr-2025

python -m venv .venv
.\.venv\Scripts\activate
source ./.venv/bin/activate


Coroutines
type of function that allow you to pause and resume execution
facilitating asynchronous programming

can yield control back to caller mid-execution allowing other tasks to run concurrently

useful
fetch data from web or reading files

implemented using async / await


asyncio.run()
creates an event loop
schedules my_coroutine
closes event loop


async   defines the coroutine
await   pause the coroutine     wait for another coroutine to complete


Concurrent execution
asyncio.gather()

can run multiple coroutines concurrently
taking advantage of asynchronous programming


Coroutines vs. Threads

Coroutines 
offer an efficient alternative to threading for I/O-bound tasks	[but not CPU tasks]
use co-operative multitasking where tasks yield control voluntarily

Threads
rely on the operating system for preemptive multitasking


Coroutine vs. Generator
Generators		iterate lazily over sequences
Couroutines		manage asynchronous workflows


Conclusion
Coroutines offer powerful lightweight solution for asynchronous programming
async / await improve code efficiency and responsiveness esp. I/O-bound tasks
to
build highly concurrent applications maximizing the speed and efficiency of programs