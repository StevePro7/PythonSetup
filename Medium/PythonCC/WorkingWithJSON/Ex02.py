# 02. Writing JSON Files
import json

data = {
    "name": "Bob",
    "age": 25,
    "is_employee": False,
    "skills": ["Java", "Spring Boot", "DevOps"],
    "projects": {
        "current": "System Upgrade",
        "completed": ["Automation", "Monitoring Setup"]
    }
}

with open("Ex02.json", "w") as file:
    json.dump(data, file, indent=4)

print("Ex02.json daved")