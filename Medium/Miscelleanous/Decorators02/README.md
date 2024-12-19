Understanding Python’s @ Decorator using Real-World Examples
16-Dec-2024

https://medium.com/@ccpythonprogramming/understanding-pythons-decorator-using-real-world-examples-8313b5292870

python -m venv .venv
.venv\Scripts\activate

python3 -m venv .venv
source .venv/bin/activate


Ex01.
Logging Function Calls


Ex02.
Authentication for a Web Application

pip install flask

curl -H "x-api-key: mysecurekey123" http://127.0.0.1:5000/secure-data


Ex03.
Caching Results


NOTES
Decorator
feature to modify / extend  behavior of methods
without altering source code

Examples
Logging
validation
Caching


Decorator
higher order function that takes another function as input
adds functionality to it and returns the modified Function

i.e.
warps a function
altering its behavior without changing its core logic


Conclusion
All examples the @ decorator modifies the behavior of the target
function by wrapping it inside another function (the wrapper)

The wrapper [function] can
- add new functionality 	e.g. logging, authentication
- modify inputs or outputs
- enforce pre-conditions 	e.g. check API keys
- improve performance		e.g. caching


Decorator
acts as a middleman between the caller and the original Function
enhancing or altering the behavior without changing the function's
source code