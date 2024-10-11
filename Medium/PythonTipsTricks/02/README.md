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