8 Confusing Python Concepts That Frustrate Most Developers
16-Apr-2025

https://medium.com/coding-nexus/8-confusing-python-concepts-that-frustrate-most-developers-with-simple-examples-469a49c92462

python -m venv .venv
source .venv/bin/activate
.\.venv\source\activate


1. The is vs == Confusion
==  checks if two values are equal
is  checks if two objects have the same memory location


2. Mutable Default Arguments
classic Python bug
mutable objecs like list or dict used as default args in functions

fix = set mutable object to None then check


3. Indentation Sensitivity
in Python if indentation is inconsistent then you'll get an error
Tip: always use tabs consistently
def: 4x spaces = indent


4. The Global Interpreter Lock (GIL)
GIL allows only one thread to execute Python bytecode at a time
in a single-process preventing true parallelism for CPU-bound tasks

Even though we start two threads, the GIL ensures they don’t run in parallel for CPU-bound
work, so the total time is similar to running count() twice sequentially—no speedup is achieved.

Tip: Use multiprocessing for CPU-heavy tasks instead of threading. Here’s how:
import multiprocessing


5. Chained Assignment
chained assignment can lead to unexpected behaviour with mutable objects
Here
since a and b share the exact memory location then modifying a also affects b


6. Closures and Late Binding
when using lambda functinos in loops Python applies late binding
this means variables are looked up when the function is executed but not defined
Here
each lambda uses the final value of i (2) instead of capturing its value at each iteration


7. Duck Typing
Python follows duck typing:
“If it looks like a duck and quacks like a duck, it must be a duck.”
Here
this means Python doesn't check explicity types but checks if an object has the expected methods

Even though Dog is not a Duck it works because Dog has a quack() method
Tip:
be mindful when relying on duck typing as it can lead to 
unexpected behaviour if objects don't fully support expected methods


8. Unpacking with *
Python allows unpacking of lists and tuples using * 
but it can be tricky in some cases
Here
use * to capture extra values
i.e.
b captures the middle values as a list


SUMMARY
1.  Use == for value comparison and is for identity complarison