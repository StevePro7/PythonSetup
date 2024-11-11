How to Use *args and **kwargs in Python

11-Nov-2024

https://medium.com/pythons-gurus/how-to-use-args-and-kwargs-in-python-04307573c7f6

*args           TUPLE
pass a flexible number of arguments to a function
positional arguments

*args parameter
function accepts any number of arguments as a tuple
collects all positional arguments pass to function as tuple


**kwargs        DICTIONARY
pass a dictionary of keyword arguments to a function
keyword arguments   arbitrary number

**kwargs parameter
collects all keyword arguments into a dictionary
allows function to handle variable number of name arguments


COMBINATION
function can handle both positional and keyword arguments

PRACTIAL
exmple = logging functino
handles various types of log messages with different log levels


CONCLUSION

*args
pass an arbitrary number of positional arguments as a tuplo
e.g.
- process lists of items
- aggregate values
- perform operations on varying sets of inputs

**kwargs
pass a variable number of keyword arguments as a dictionary
e.g.
- configuration settings
- optional parameters
- and any case where named arguments enhance clarity and functionality
