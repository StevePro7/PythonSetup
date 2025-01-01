# 07. Checking for Keys
import json

json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'
python_data = json.loads(json_string)

key: str = "skills"
if key in python_data:
    print(f"Skills: {python_data[key]}")
else:
    print(f"Key '{key}' not found")