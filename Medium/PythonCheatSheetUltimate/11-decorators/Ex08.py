# 08. Decorator with Optional Arguments
from functools import wraps

def smart_decorator(arg=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arg:
                print(f"Argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    if callable(arg):
        return decorator(arg)
    return decorator


@smart_decorator
def no_args():
    print("No args")


@smart_decorator("With args")
def with_args():
    print("With args")


no_args()
with_args()