I created 5 different lambda functions in Python. They all returned 4. I’m not okay
17-Dec-2025

https://medium.com/@anas-issath/d71e6578b8f8

Late Binding
funcs = [lambda: i for i in range(5)]

Python does not capture the value of variables - it captures the name

Late Binding
variable binding happens late - when the function is called NOT when it's created
all 5x functions use same variable "i" which equals 4 so they return 4


BUGS

Bug #1: Button callbacks
# Create buttons with numbers 0-9
buttons = []
for i in range(10):
    button = Button(text=str(i), command=lambda: print(i))
    buttons.append(button)
# Every button prints 9

Bug #2: Event handlers
# Attach handlers to elements
for i, element in enumerate(elements):
    element.onclick = lambda: handle_click(i)
    # All handlers pass the last index

Bug #3: Async tasks
# Queue up tasks
tasks = []
for i in range(5):
    tasks.append(asyncio.create_task(process(i)))
    # If process() is a lambda, same problem


FIX
Early Binding with Default Arguments

Solution 1: Default argument trick (most common)
Ex02a
default arguments are evaluated when the function is defined not when it's invoked

Left i:     parameter name (local to the lambda)
Right i:    current value from the loop (captured at definition time)


Solution 2: functools.partial
Ex02b
partial creates a new functino with the argument pre-filled
no late binding


Solution 3: Use a closure factory
Ex02c
each call to make_func creates a new scope with its own "x"
inner lambda captures that specific "x"


Solution 4: Just avoid lambdas in loops
Ex02d


Closures
Python design decision: closures captures variables by reference NOT by value
Python chose references. Always. No exceptions


IMPORTANT
How to spot this in Code Reviews

# DANGER: Lambda in loop without default argument
[lambda: x for x in items]
[lambda: process(i) for i in range(n)]

# SAFE: Lambda with default argument
[lambda x=x: x for x in items]
[lambda i=i: process(i) for i in range(n)]


SUMMARY
Just remember: functions remember names, not values
And remember: lambda: i is not your friend. lambda i=i: i is!
