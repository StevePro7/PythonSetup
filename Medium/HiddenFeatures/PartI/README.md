Python: Hidden Features — part 1
31-Aug-2024


1. Function Objects
Everything in Python is an object including functions

default parameters in function are evaluated
when the function is defined

Issue: mutable default parameter
can modify [mutable default] parameter for future calls to function

SOLUTION
Def add_subject(name, subject, subjects=None):
    if subjects is None:
        subjects = []

    subjects.append(subject)

this lets you avoid the unexpected behavior of mutating the same object.


2. Make class object behave like a Function
If you want to make class object callable i.e. behave like function then
define the __call__ method.  This allows to define behavior of object
when invoked like a function

This allows you to use a class objet in contexts where a callable is
expected - e.g. using a class as a decorator for instance


3. String Method
rather than use startswith and endswith to match substring

instead pass multiple substrings as a tuple to these methods
this prevents from writing multiple conditions while preserve
same functionality


4. Use Frozenset
remember that set is mutable

but
frozenset = immutable set
elements cannot be changed after creation
have safety used as dictionary key
[dicts keys are immutable]


5. Pickle Files
pickes used to dump data objects to disk but usually one object per pkl file
However store as manay objects w/in single pkl file
Plus when reload not necessary to load all the objects

dump objects w/in same context manager
using with