# 03. Using functools.wraps
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Wrapper function"""
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def greet(name: str):
    print(f"hi! {name}")


print(greet.__name__)
print(greet.__doc__)
