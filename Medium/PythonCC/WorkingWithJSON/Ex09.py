# 09. Adding or Removing Keys
import json

json_string = '{"name": "Charlie", "age": 35, "skills": ["C++", "Rust"]}'
python_data = json.loads(json_string)
print(python_data)

python_data["department"] = "Data Science"
print(python_data["department"])  # Output: Data Science
print(python_data)

del python_data["age"]
print(python_data)  # The 'age' key will no longer be in the data