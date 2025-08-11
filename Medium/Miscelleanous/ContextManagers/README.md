Understanding Context Managers in Python: A Practical Guide
https://mahdijafaridev.medium.com/understanding-context-managers-in-python-a-practical-guide-f785ee483c8d

Ex01
__enter__(self)
__exit__(self, exc_type, exc_value, traceback)


Writing classes with __enter__ and __exit__ can be verbose
Use @contextmanager decorator from contextlib package
Ex02


When to Use Custom Context Managers
* Managing database connections or sessions
* Acquiring and releasing locks or semaphores
* Temporarily modifying global settings or environment variables
* Timing code execution for profiling
* Handling temporary files or network connections


Example: Timer Context Manager Using contextlib
Ex03


Asynchronous Context Managers
__aenter__()
__aexit__()
decorator @contextlib.asynccontextmanager
Ex04