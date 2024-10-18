# 04. Class Decorator
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("beg")
        self.func(*args, **kwargs)
        print("end")


@MyDecorator
def greet(name: str):
    print(f"hi! {name}")


greet("adriana")
