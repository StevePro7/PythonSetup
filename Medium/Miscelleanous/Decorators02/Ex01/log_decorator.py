import datetime

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"{datetime.datetime.now()}: Calling {func.__name__} with '{args}' and '{kwargs}'")
        result = func(*args, **kwargs)
        print(f"{datetime.datetime.now()}: {func.__name__} returned ''{result}''")
        return result
    return wrapper