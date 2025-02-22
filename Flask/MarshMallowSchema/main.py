from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import json


# Define a simple dataclass
@dataclass()
class User:
    name: str
    email: str


# Define a Marshmallow schema for the User dataclass
UserSchema = class_schema(User)()


# Create a User object
user = User(name="John Doe", email="john.doe@example.com")


# Serialize the User object to a dictionary
user_dict = UserSchema.dump(user)

# Serialize the dictionary to a JSON string
user_json = json.dumps(user_dict, indent=4)
print("Serialized JSON:")
print(user_json)


# Deserialize the JSON string back to a dictionary
user_dict_from_json = json.loads(user_json)

# Deserialize the dictionary back to a User object
user_obj = UserSchema.load(user_dict_from_json)

print("\nDeserialized JSON:")
print(f"Name: '{user_obj.name}', Email: '{user_obj.email}'")