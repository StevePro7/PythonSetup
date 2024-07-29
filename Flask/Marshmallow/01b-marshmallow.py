from marshmallow import Schema, fields, post_load
import json

# Define the User class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f'User(name={self.name}, email={self.email}, age={self.age})'

# Define the UserSchema
class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# Sample JSON data
# user_json = '''
# {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "age": 30
# }
# '''
user_json: str = '{"name": "JohnZ Doe","email": "johnX.doe@example.com","age": 29}'
# Parse JSON string into Python dictionary
user_data = json.loads(user_json)

# Create an instance of UserSchema
schema = UserSchema()

# Deserialize JSON data to User object
user = schema.load(user_data)

# Print the User object
print(user)
user.age = 27
print(user)