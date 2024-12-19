import functools

def cache(func):
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            print("Returning cached result")
            return memo[args]

        print("Calculating result")
        result = func(*args)
        memo[args] = result
        return result
    return wrapper