from typing import TypeVar

T = TypeVar('T')

def echo(value: T) -> T:
    return value


print(echo(42))     # Output: 42
print(echo('Hi'))   # Output: Hi