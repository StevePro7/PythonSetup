Async Programming in Python: Part 2 — Advanced Patterns and Techniques
03-Aug-2025

https://mskadu.medium.com/async-programming-in-python-part-2-advanced-patterns-and-techniques-7f6b65061b74

GitHub
https://github.com/mskadu/async-programming-python

SAMPLES
pip install requests
pip install aiohttp


Tools
Semaphores: Control Resource Access
limit how many operations run simultaneously on shared resource
e.g.
network connection

Semaphore = bouncer at nightclub
prevents resource exhaustion
e.g.
rate-limited APIs
connection pools


Queues: Producer-Consumer patterns
co-ordinate work between
producer    create tasks
consumer    process them

decouples [separates] work creation from work processing
allows different rates or production and consumption


Locks: Protecting Shared Resources
prevent race conditions
when multiple coroutines need to access shared resources safely

lock ensures atomic access to shared resource


Production Error Handling
Pattern 1: Timeout Patterns
Pattern 2: Exception Handling in Concurrent Operations
Pattern 3: Retry Mechanisms


Integration with Synchrounous Code
Thread Pool Integration
allows you to use any synchronous library within async applications
without blocking the event loop

Method
wrap sync calls with loop.run_in_executor()
use ThreadPoolExecutor for I/O-bound sync operations
use ProcessPoolExecutor for CPU-bound sync operations


EXAMPLE
Resource management
Concurrency control
Producer-Consumer pattern
Error handling
Batch processing
Component separation


Custom Event Loop Management
Event Loop
software design pattern for handling system events concurrently
unclog blocking operations - let multiple operations execute in "parallel"

IMPORTANT
set Env Var
PYTHONASYNCIODEBUG=1


Performance Optimisation (Brief Overview)
Pitfalls
blocking event loop
creating too many tasks
memory leaks


Essential Tools and Techniques
Profiling async code:
aiomonitor
py-spy
asyncio debugging   asyncio.get_event_loop().set_debug(True)

Memory + performance
asyncio-mqtt
Grafana + Prometheus


Summary
async programming not always the right choice

use async when you have genuine concurrency needs:
multiple I/O operations, handling simultaneous requests, co-ordinating independent tasks

sync programming can be better for CPU-bound work or linear processing 
