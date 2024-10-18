# 07. Stacking Decorators
from functools import wraps

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("beg")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@my_decorator
@repeat(2)
def greet(name: str):
    print(f"Hi! {name}")


greet("stevepro")