import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.4f} seconds")

with timer():
    total = sum(i * i for i in range(10**6))


# OUTPUT
# Elapsed time: 0.1357 seconds