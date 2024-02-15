asyncio
13-Feb-2024

https://realpython.com/async-io-python

TODO
https://realpython.com/python-concurrency
https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5
https://www.dabeaz.com/coroutines


Coroutine
specialized generator functions
a Coroutine is a specialized version of a generator functions
a Coroutine is a function that can supsend its execution before reaching return
and indirectly pass control to another coroutine for some time

async
native Coroutine
asynchronous generator function

await
passes control back to the evnet loop to let something else run
signal that marks a break point: lets Coroutine suspend and resume later

saync def = Coroutine

awaitable
object that is another Coroutine

generator
pauses each time it hits a yield and goes no further

Event Loop
while true loop that monitors coroutines

asyncio.run()
responsible for getting event loop, running tasks until they are marked complete
forces execution by scheduling the main() coroutine [future objecdt] for execution on event loop

 

countasync
1s vs. 3s


@asyncio.coroutine
DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead



IMPORTANT
wanted to know the address of variable in Python

reference
https://www.geeksforgeeks.org/python-program-to-find-and-print-address-of-variable