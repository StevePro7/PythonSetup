Async Programming in Python: Part 1 The Fundamentals
03-Aug-2025

https://python.plainenglish.io/async-programming-in-python-part-1-the-fundamentals-60cb280c6533

GitHub
https://github.com/mskadu/async-programming-python


Coroutines
async keyword
transforms regular function into a coroutine function
marks function as "async-capable"

e.g.
# Regular function
def regular_function():
    pass

# Coroutine  function
async def async_function():
    pass


Coroutine functions
can pause and resume its execution
when you call async function you get a coroutine object not the result

coroutine
represents the "potential" to run the async function


WHEN
best suited for any operation that involves waiting:
network requests, file I/O, database queries, external API calls

But NOT
when next step relies on the output of these operations


Run coroutine
asyncio.run()
creates an event loop, runs your coroutine and cleans up
recommended entry point for async programs


Patterns
Pattern 1: Async Data Processing
Pattern 2: Async Context Management
Pattern 3: Task Creation and Management


Summary
async excellent for
I/O-bound operations
network requests, file operations, database queries

Server applications
handling many simultaneous requests without blocking


async NOT great for
CPU-intensive tasks
math calculations, data processing, image manipulation
need actual parallel processing NOT concurrent waiting


Async programming
make better use of waiting time
when code waits for resources then async transforms idel time into productive concurrency