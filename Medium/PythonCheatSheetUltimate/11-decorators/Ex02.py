# 02. Decorator with Arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("beg")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


@my_decorator
def greet(name: str):
    print(f"hi! {name}")


greet("stevepro")
