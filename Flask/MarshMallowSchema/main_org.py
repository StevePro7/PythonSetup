from marshmallow import Schema, fields, post_load
import json


# Define a simple class
class User:
    def __init__(self, name, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User (name={self.name}, email={self.email})>"


# Define a schema for the User class
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Str()

    @post_load
    def manke_user(self, data, **kwargs):
        return User(**data)


# Create a User object
user = User(name="John Doe", email="john.doe@example.com")

# Create a UserSchema instance
user_schema = UserSchema()


# Serialize the User object to a dictionary
user_dict = user_schema.dump(user)

# Serialize the dictionary to a JSON string
user_json = json.dumps(user_dict, indent=4)
print("Serialized JSON:")
print(user_json)

# Deserialize the JSON string back to a dictionary
user_dict_from_json = json.loads(user_json)

# Deserialize the dictionary back to a User object
user_obj = user_schema.load(user_dict_from_json)

print("\nDeserialized JSON:")
print(f"Name: '{user_obj.name}', Email: '{user_obj.email}'")