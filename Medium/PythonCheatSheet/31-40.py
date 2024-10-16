# 31.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
union_set = set1 | set2
# Intersection
intersection_set = set1 & set2
# Difference
difference_set = set1 - set2


# 32.
numbers = [1, 2, 3, 4, 5]
# Squares of even numbers
squares = [x**2 for x in numbers if x % 2 == 0]


# 33.
add = lambda x, y: x + y
result = add(3, 5)


# 34.
from concurrent.futures import ThreadPoolExecutor
def square(x):
    return x**2
with ThreadPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])


# 35.
import gettext
# Set language
lang = 'en_US'
_ = gettext.translation('messages', localedir='locale', languages=[lang]).gettext
print(_("Hello, World!"))


# 36.
# Create a virtual environment
python -m venv myenv
# Activate virtual environment
source myenv/bin/activate  # On Unix/Linux
myenv\Scripts\activate  # On Windows
# Deactivate virtual environment
deactivate


# 37.
from datetime import datetime, timedelta
now = datetime.now()
# Format date
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
# Add days to a date
future_date = now + timedelta(days=7)


# 38.
my_dict = {'name': 'John', 'age': 30}
# Get value with default
age = my_dict.get('age', 25)
# Iterate over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")


# 39.
import re
text = "Hello, 123 World!"
# Match numbers
numbers = re.findall(r'\d+', text)


# 40.
def square_numbers(n):
    for i in range(n):
        yield i**2
squares = square_numbers(5)
