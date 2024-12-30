# 10. Real-World Use Case: Extracting Keys
import json

def extract_keys(obj, parent_key=""):
    keys = []
    for key, value in obj.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        keys.append(full_key)
        if isinstance(value, dict):
            keys.extend(extract_keys(value, full_key))
    return keys


json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'
python_data = json.loads(json_string)

all_keys = extract_keys(python_data)
print(all_keys)