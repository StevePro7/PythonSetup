from typing import Annotated
from pydantic import Field, TypeAdapter, ValidationError

PositiveInt = Annotated[int, Field(gt=0)]
adapter = TypeAdapter(PositiveInt)
print(adapter.validate_python(5))

try:
    adapter.validate_python(-1)
except ValidationError as e:
    print(e)