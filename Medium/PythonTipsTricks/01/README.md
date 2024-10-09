Useful Python tips and tricks — #1
09-oCT-2024

https://medium.com/@johnidouglasmarangon/useful-python-tips-and-tricks-1-f5fdabe8feb4


01- Ellipsis
Ellipsis = 3 dots (...)
represent an infinitive or something unspecified

Can replace pass keyword with ellipses


02. Merge dictionaries
two ways:
one using dobule star **    all items unpacking
two merge operator |        Python 3.9


03. Decorators with classes
decorator lets you add functionality w/o modifying source code
decorator shorthand way of calling higher order functions

decorators can be created using classes or functions
end result is the same except classes can explore OOP concepts


04. Save memory with generators
generator pattern allows you to get values lazily (on demand)
thus saving memory usage

If you have a large list then consider using generators to save memory
NB:
generator expression == generator comprehension

04b. generator function
statement that returns lazy iterator to iterate over values on demand
very useful for large sequence of values and don't need to store them all in memory

