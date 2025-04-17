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