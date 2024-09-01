list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

target_name = 'Alice'

person = next((item for item in list_of_dicts if item.get('name') == target_name),  "person not found." )
print(f"Found: {person}")