from cache_decorator import cache

@cache
def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))
    print()
    print()
    print()
    print(fibonacci(10))  # This will return the cached result