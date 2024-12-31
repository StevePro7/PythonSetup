# 08. Listing All Keys
import json

json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'
python_data = json.loads(json_string)

keys = python_data.keys()
print(keys)