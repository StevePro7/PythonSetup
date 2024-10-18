# 09. Class Method Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("beg")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


class MyClass:
    @staticmethod
    @my_decorator
    def static_method():
        print("Static method called")


MyClass.static_method()