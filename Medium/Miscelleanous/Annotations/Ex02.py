def add_numbers(x: int, y: int) -> int:
    return x + y


print(add_numbers.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
