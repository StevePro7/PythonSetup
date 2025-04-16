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