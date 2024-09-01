Python: Hidden Features — part 1I
31-Aug-2024


Python: Hidden Features — part 2
https://pravash-techie.medium.com/python-hidden-features-part-2-7d59bbef57ae


1. use next()
typically use for each loop to find target in dictionary
more concise way of doing this is using next()

next() is built-in function
retrieves next item from an iterator
part of Python iterator protocol
[also includes iter() to object iterator from iterable => list, tuple, string]

next()
returns next item
OR
StopIteration unless default value provided


2. Use StringIO instead of (+) operator
similar to StringBuilder in C#/.NET vs. "+=" for string concatenation 


3. use properties
instead of getter and setter functions

# def set_x(self, x):
#     self._x = x
AttributeError: 'ObjectDef' object has no attribute 'set_x'

# @x.setter
# def x(self, val):
#     self._x = val
AttributeError: can't set attribute


4. list.reverse() vs list[::-1]
list.reverse()
reverses original list in-place

list[::-1]
creates a new list and reverses the new list leaving the original list intact
i.e.
creates copy thus uses twice the memory


5. using else in for/while loop
don't always need a flag to find an item
as per the modified code