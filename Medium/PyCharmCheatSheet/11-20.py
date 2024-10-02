# 11.
squares = [x**2 for x in range(5)]


# 12.
add = lambda x, y: x + y
result = add(2, 3)


# 13.
# Create a virtual environment
python -m venv myenv
# Activate the virtual environment
source myenv/bin/activate  # On Unix or MacOS
# myenv\Scripts\activate  # On Windows
# Deactivate the virtual environment
deactivate


14.
# Install a package
pip install package_name
# List installed packages
pip list
# Create requirements.txt
pip freeze > requirements.txt
# Install packages from requirements.txt
pip install -r requirements.txt


15.
import json
# Convert Python object to JSON
json_data = json.dumps({"name": "John", "age": 25})
# Convert JSON to Python object
python_obj = json.loads(json_data)


16.
import re
pattern = r'\d+'  # Match one or more digits
result = re.findall(pattern, "There are 42 apples and 123 oranges.")


17.
from datetime import datetime, timedelta
current_date = datetime.now()
future_date = current_date + timedelta(days=7)


18.
numbers = [1, 2, 3, 4, 5]
# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Map
squared = list(map(lambda x: x**2, numbers))
# Reduce (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)


19.
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Get value with default
value = my_dict.get('d', 0)
# Dictionary comprehension
squared_dict = {key: value**2 for key, value in my_dict.items()}


# 20.
import threading
def print_numbers():
    for i in range(5):
        print(i)
thread = threading.Thread(target=print_numbers)
thread.start()

