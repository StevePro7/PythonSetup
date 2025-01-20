def greet(name: str, age: int) -> str:
    return f"Hello, {name}.  yOU ARE {age} years old"


print(greet.__annotations__)
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
