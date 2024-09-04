import json

class MyCustomClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"MyCustomClass(name={self.name}, age={self.age})"

def custom_decoder(dct):
    if 'name' in dct and 'age' in dct:
        return MyCustomClass(name=dct['name'], age=dct['age'])
    return dct

json_str = '{"name": "John Doe", "age": 30}'

obj = json.loads(json_str, object_hook=custom_decoder)

print(obj)  # Output: MyCustomClass(name=John Doe, age=30)
