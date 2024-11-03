Experimenting with Python threads
03-Nov-2024

Reference:
https://medium.com/@datafairy/experimenting-with-python-threads-88f66b002acf

python -m venv .venv
source .venv/bin/activate

Thread
separate flow of execution w/in program that can run concurrently
with other threads allow multiple ops to appear run simultaneously

Python viruthal machine is NOT thread-safe interpreter
i.e. interpreter can only execute one thread at any moment

GIL
limitation enforced by Global Interpreter Lock
limits one Python thread to run at a time w/in smae process
at the same time on a single processor


Threads
Good for tasks that spend much time waiting for external events
e.g. I/O bound tasks
Database    I/O
Network     I/O
File        I/O


Pitfalls
only one thread in Python

Multiple background thread cause exceptions

Set arg daemon=True to thread will flag it as background thread
But if more than one thread flagged as background then program will not work

INTERESTING
daemon=True
gives an error for me - this may be greater than Python 3.8 ??

NB: adding daemon=True to multiple functinos will result in multiple exceptions


DEFINITIONS
race conditions
When two or more threads are trying to access a shared resuor