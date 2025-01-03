import factorial
import time


def py_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * py_factorial(n-1)


# Test Python implementation
start = time.time()
result = py_factorial(900)
end = time.time()
print(f"Python factorial time: {end - start:.6f} seconds")

# Test C extension
start = time.time()
result = factorial.factorial(900)
end = time.time()
print(f"C extension factorial time: {end - start:.6f} seconds")