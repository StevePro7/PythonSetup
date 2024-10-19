import timeit
import math


def is_prime_naive(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_optimized(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print("Naive prime check:", timeit.timeit(lambda: is_prime_naive(999983), number=100))
print("Optimized prime check:", timeit.timeit(lambda: is_prime_optimized(999983), number=100))