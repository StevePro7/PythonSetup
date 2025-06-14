10 Hottest Python Tricks for Efficient Coding
14-Jun-2025

https://medium.com/@arsilmirza/10-hottest-python-tricks-for-efficient-coding-0b8fddf735bc


#1. List Comprehensions for Quick Data Processing
create lists
instead of using loops and append manually
generate them in one line

EX
# Traditional approach
squares = []
for i in range(10):
    squares.append(i**2)

# Using list comprehension
squares = [i**2 for i in range(10)]


#2. Using zip() Parallel Iteration
zip() allows you to iterate over multiple lists in parallel
pairs elements from each list together until shortest list ends

EX
names = ['Ali', 'Boby', 'Charles']
ages = [14, 50, 18]

for name, age in zip(names, ages):
    print(f'{name} is {age} years old.')
	
	
#3. Dictionary Comprehensions for Clean Data Transformation
create dictionaries in a more brief and readable way

EX
# Creating a dictionary using dictionary comprehension
names = ['Ali', 'Boby', 'Charles']
ages = [14, 50, 18]
age_dict = {name: age for name, age in zip(names, ages)}

print(age_dict)


#4. Use Enumerate to Get Index and Value Together
enumerate() returns index and value from list or tuple when iterating

EX
names = ['Ali', 'Boby', 'Charles']
for index, name in enumerate(names):
    print(f'{index}: {name}')
	
	
#5. The Power of {collections.defaultdict}
defaultdict subclass built-in dictionary
simplifies handling keys not in dictionary
when access missing key defaultdict create it with default value

EX
from collections import defaultdict

# Default type is list, meaning missing keys will have a default value of an empty list
default_dict = defaultdict(list)

# Appending to a missing key automatically creates the key
default_dict['fruits'].append('apple')
default_dict['fruits'].append('banana')

print(default_dict)


#6. Named Tuples for Cleaner Code
creates tuple-lie objects with named fields
lightweight alternative to classes while has clear structure

EX
from collections import namedtuple

# Define a named tuple for a Point
Point = namedtuple('Point', 'x y')
p = Point(10, 20)

print(p.x, p.y)


#7. Using itertools for Memory-Efficient Iterations
itertools provides set of fast memory0-efficient tools
for working with iterators e.g. count(), cycle(), repeat(), chain()

EX
import itertools

numbers = [1, 2, 3]
combinations = list(itertools.combinations(numbers, 2))

print(combinations)


#8. Context Managers and the with Statement
manage resources file handling database connections more efficiently
with statement simplifies resource management = clean up after use

EX
# Without context manager
file = open('example.txt', 'r')
content = file.read()
file.close()

# With context manager
with open('example.txt', 'r') as file:
    content = file.read()
	
	
#9. Lambda Functions for Quick One-Liners
lambda functions allow you to create small anonymous functions on the fly

EX
# Sort a list of tuples by the second element using a lambda function
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)


#10. F-Strings for Readable and Efficient String Formatting
formatted string literals f-strings more advanced and effective
method to format strings - perform better than str.format()

EX
name = 'Ali'
age = 14
print(f'{name} is {age} years old.')