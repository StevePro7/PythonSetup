list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

target_name = 'Bob'

for person in list_of_dicts:
    if person['name'] == target_name:
        print(f"Found: {person}")
        break  # Exit the loop once the target is found
else:
    print("Target not found.")