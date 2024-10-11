Useful Python tips and tricks — #2
09-oCT-2024

https://medium.com/@johnidouglasmarangon/useful-python-tips-and-tricks-2-63c48d88e3b8


01. Else Conditional statement with loop
use an else statement with for/while-loop to execute code when loop terminates
regardless whether loop was executed
NB: used infrequently


02. Parameterizing test functions in pytest
parameterize is a pytest marks decorator used to execute the same test
function multiple times with different set or arguments

NB: third set of parameters use xfail mark to define failure argument


03. List Comprehensions with Nested Loops
list comprehension is a way to avoid nested loops combining multiple
for-loops in a single line of code


04. Use tqdm to iter on loops
tqdm is Python library to provide simple way to add progress bar to loops
Recommended for long-running process to show visual cue to user about progress status


05. Generic Functions
A mechanism which allows functions to operate same behavior with multiple types
maintaining relations btwn them e.g. arguments, name, return values


06. Use PyPi Test repository
PyPi Test is version of PyPi repo for testing purposes
can be used to practice and learn how to publish a package to Python ecosystem
before releasing it

https://test.pypi.org
https://packaging.python.org/en/latest/guides/using-testpypi

PyPi Test has separate databsse from PyPi repo
create an account to publish your packages


07. Using Context Manager
context manager is a way to manage resources
setup and teardown resources automatically when they are no longer needed

Two special methods:
__enter__()		called when code block entered
__exit__()		called when code block exited	used to return resource instance

To use context manager with generator you need to define a function
and use the yield state to return the instance

When the code block is exited the code after the yield statement is executed


08. Timing
Timing = method to measure the execution time of a piece of code
timeit 
built-in Python module that provides a simple way to run a piece of code to get
execution time
Example
python-m timeit --n [number] -s [setup] [stmt]


09. The Walrus operator
Since Python 3.8 special assignment expression known as walrus operator (:=)
syntax allows you to assign values to variables within expression and use it

Walrus operator does not necessarily improve readability or efficiency in code
NB: is usual better to write code in a traditional manner


10. Using an Entrypoint
Recommended to make code more readable and intuitive to use entrypoint
if __name__ == '__main__':