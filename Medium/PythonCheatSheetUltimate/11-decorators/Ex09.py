# 09. Class Method Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("beg")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


class MyClass:
    @classmethod
    @my_decorator
    def class_method(cls):
        print("Class method called")


MyClass.class_method()