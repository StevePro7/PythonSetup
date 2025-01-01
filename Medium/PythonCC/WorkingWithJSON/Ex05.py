# 05. Accessing Keys
import json

json_string = '''
{
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis"],
    "projects": {
        "current": "Data Migration",
        "completed": ["API Development", "Web Scraping"]
    }
}
'''

data = json.loads(json_string)

print(data["name"])
print(data["projects"]["current"])