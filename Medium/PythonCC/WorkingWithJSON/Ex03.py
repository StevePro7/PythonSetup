# 03. Working with Nested JSON
import json

with open("Ex03.json", "r") as file:
    data = json.load(file)

api_details = data["projects"]["details"]["API Development"]
print(f"API Development Duration: {api_details['duration']}")
print(f"Team Size: {api_details['team_size']}")
