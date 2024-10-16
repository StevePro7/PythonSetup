# 21.
import asyncio
async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)
asyncio.run(print_numbers())


# 22.
from bs4 import BeautifulSoup
import requests
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.text


# 23.
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)


# 24.
import unittest
def add(x, y):
    return x + y
class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
if __name__ == '__main__':
    unittest.main()


# 25.
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# Execute SQL query
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
# Commit changes
conn.commit()
# Close connection
conn.close()


# 26.
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, Python!')
# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()


# 27.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This block always executes.")


# 28.
import json
data = {'name': 'John', 'age': 30}
# Convert Python object to JSON
json_data = json.dumps(data)
# Convert JSON to Python object
python_object = json.loads(json_data)


# 29.
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@decorator
def my_function():
    print("Inside the function")
my_function()


# 30.
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
union_set = set1 | set2
# Intersection
intersection_set = set1 & set2
# Difference
difference_set = set1 - set2
