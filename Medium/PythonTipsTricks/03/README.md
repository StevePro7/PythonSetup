Useful Python tips and tricks — #3
09-oCT-2024

https://medium.com/@johnidouglasmarangon/useful-python-tips-and-tricks-3-0f54f8258992

01. lru_cache
Function caching
store results of expensive or frequently called function calls and cache result
improve performance of functions called repeated w/ same args reducing unnecc computation
e.g.
functools.lru_cache
LRU
Least Recently Used retain most recent results and discard oldest ones


02. pydantic
Pydantic settins module provides clean + efficient way to handle configurations
by auto load + validate settings from environment variables .env files or default values
e.g.
pip install -q pydantic-settings


03. Descriptors
Descriptors are powerful feature in Python that allow customization of attribute
access.  Descriptor can be used for validation, cahcing or lazy loading

A descriptor is an object that implements one or more methods
__get__()
__set__()
__delete__()

which manage the behavior of attribute access

Descriptors can be used to define properties, manage access control and
enforce constraints on class attributes

Understanding descriptors can help you write more flexible and maintainable
object-orientated code in Python


04. Pickling and Unpickling
Pickling    process of serializing Python object into byte stream saved to file
Unpickling  reverse process byte stream is converted back into Python object

pickle.dump()   save binary data
pickle.load()   load binary data

Security
be cautious when unpickling data from untrusted sources as it can potentially
execute arbitrary code

Efficiency
Pickling is efficient for simple data types but can be slower and less
portable compared to other serialization formats like JSON

Pickling is esp. useful when you want to save state of an object and
reload it later without losing any information


06. Invert Magic function
__invert__ is a special method in Python also known as the bitwise NOT
magic method
7. 
It is used to implement bitwise NOT operator (~) for objects that support it
When you appled the ~ operator to an object Python auto calls __invert__()
method passing the object itself as the argument

The method should return a new object that represents bitwise inversion
of the original one

__invert__ demos how objects can be customized for objects that do not support
the bitwise NOT operation offering flexibility in handling such operators