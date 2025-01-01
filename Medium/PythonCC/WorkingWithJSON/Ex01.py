# 01. Reading JSON Files
import json

with open("Ex01.json", "r") as file:
    data = json.load(file)

print(f"Name: {data['name']}")
print(f"Name: {data['projects']['current']}")
