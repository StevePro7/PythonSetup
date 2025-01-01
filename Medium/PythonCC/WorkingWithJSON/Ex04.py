# 04. Converting JSON Strings to Python Objects
import json

json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'

python_data = json.loads(json_string)
print(f"Name: {python_data['name']}")

json_output = json.dumps(python_data, indent=2)
print(json_output)