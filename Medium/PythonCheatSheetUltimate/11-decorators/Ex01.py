# 01. Basic Decorator
def my_decorator(func):
    def wrapper():
        print("beg")
        func()
        print("end")
    return wrapper


@my_decorator
def say_hi():
    print("hi!")


say_hi()
