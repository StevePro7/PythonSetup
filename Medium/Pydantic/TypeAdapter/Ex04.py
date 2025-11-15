from typing import List
from pydantic import TypeAdapter, BaseModel

class Item(BaseModel):
    id: int
    name: str

raw = [
    {"id": 1, "name": "A"},
    {"id": "2", "name": "B"},
]

adapter = TypeAdapter(List[Item])
items = adapter.validate_python(raw)
print(items)