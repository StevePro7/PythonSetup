from dataclasses import dataclass
from marshmallow_dataclass import class_schema


# Define a simple dataclass
@dataclass()
class User:
    name: str
    email: str


# Define corresponding schema
UserSchema = class_schema(User)()
