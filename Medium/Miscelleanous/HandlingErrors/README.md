Handling Errors in Python: Try-Except, Custom Exceptions, and More
14-Jan-2025

https://medium.com/@mathur.danduprolu/handling-errors-in-python-try-except-custom-exceptions-and-more-26a6aa436d20

SyntaxError
print("Hello World'

TypeError
operation performed on incompatible types
result = "Hello" + 5

ValueError
argument of the correct type but inappropriate value
num = int("abc")

IndexError
index out of range
lst = [1, 2, 3]
print(lst[5])

KeyError
dictionary key that doesn't exist
dct = {"name": "Alice"}
print(dct["age"])


LOGGING
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    with open('non_existent_file.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    logging.error("File not found.")


Use specific exceptions rather than general Exception

Avoid silent failures e.g. empty except blocks

Leverage custom exceptions for domain-specific errors

Implement logging for better error tracking

Graceful shutdown - use finally for cleanup tasks
e.g. close files or database connections