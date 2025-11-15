from typing_extensions import TypedDict
from pydantic import TypeAdapter, ValidationError

class User(TypedDict):
    name: str
    id: int

adapter = TypeAdapter(list[User])
users = adapter.validate_python([{"name": "Fred", "id": "3"}])
print(users)

try:
    adapter.validate_python([{"name": "Fred", "id": "oops", "extra": "ignored"}])
except ValidationError as e:
    print(e)