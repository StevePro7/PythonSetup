from log_decorator import log_function_call

@log_function_call
def add_numbers(x, y: int) -> int:
    return x + y

if __name__ == "__main__":
    result: int = add_numbers(5, 10)
    print(result)