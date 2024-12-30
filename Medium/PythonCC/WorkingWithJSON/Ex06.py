# 06. Iterating Over Keys
import json

json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'
python_data = json.loads(json_string)

for key in python_data:
    print(f"Key: {key}, Value: {python_data[key]}")