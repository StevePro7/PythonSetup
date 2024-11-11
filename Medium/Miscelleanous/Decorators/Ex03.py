def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b: int) -> int:
    return a + b

print(add(5, 3))