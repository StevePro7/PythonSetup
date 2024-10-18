# 06. Method Decorator
from functools import wraps

def method_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print("MD")
        return func(self, *args, **kwargs)
    return wrapper


class MyClass:
    @method_decorator
    def meet(self, name: str):
        print(f"Hi {name}")


obj = MyClass()
obj.meet("suzanne")
