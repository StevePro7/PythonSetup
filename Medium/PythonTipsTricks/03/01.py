import time
from functools import lru_cache

@lru_cache(maxsize=12)      # Cache 12 unique results
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Running first time with cache
start = time.time()
print(fibonacci(35))  # Takes more than 5 seconds the first time
print(f"Time: {time.time() - start:.2f} seconds")

# Running the cached result
start = time.time()
print(fibonacci(35))  # Returns immediately from cache
print(f"Time: {time.time() - start:.2f} seconds")
