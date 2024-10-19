Python Performance Optimization: A Comprehensive Guide
19-Oct-2024

https://blog.devgenius.io/python-performance-optimization-a-comprehensive-guide-21bc4f40dcfd


PROFILING
Ex01
cProfile


SnakeViz
pip install line_profiler
python -m cProfile -o profile.prof Ex01.py
snakeviz profile.prof


Line Profiler
pip install line_profiler
Ex02
kernprof -l -v Ex02.py


Memory Profiler
pip install memory_profiler
Ex03
python -m memory_profiler Ex03.py


CODE OPTIMIZATION
01. Lists vs. Sets
when you need to test if item in collection then sets are faster than lists

Ex04
weird - test took longer!
List membership: 2.4433426670000244
Set membership: 3.3293638309999096

Ex05
Dict lookup
weird - test took longer!
List lookup: 13.762723470000083
Dict lookup: 22.735888665000175

Ex06
Algorithm
Naive       prime check: 3.701558549999845
Optimized   prime check: 0.004547948999970686

Ex07
List comp