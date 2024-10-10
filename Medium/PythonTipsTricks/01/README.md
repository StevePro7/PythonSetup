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


05. Sort dictionary by values
Pythonic way to access dictionary values = itemgetter() method


06. Use stopwords from spaCy
Stopwords = list of words that has no meaning or relevance in a text
Common task in text pre-processing is to remove stopwords to clean up the text

ModuleNotFoundError: No module named 'spacy'
python -m pip install spacy


08. Convert a list to a namedtuple
namedtuple creates an immutable tuple with named fields and allow access via dot notation
_make method = iterable that creates namedtuple from a list


09. Parsing URL
urlparse method extracts components of URL e.g. domain, user, password


10. Match
Python 3.10 use match to execute switch case statement rather than long if-elif chains
NB: the _ (underscore) is a wildcard patterh that matches any value