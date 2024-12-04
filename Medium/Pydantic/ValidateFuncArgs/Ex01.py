
from datetime import datetime
from pydantic import validate_call, ValidationError


@validate_call
def validate_mixed_types(count: int, name: str, tags: list[str]) -> None:
    pass


try:
    validate_mixed_types(
        count="123", name=None, tags=["valid", datetime.now()]  # Second item should be str
    )
except ValidationError as validation_error:
    print("Validation errors:")
    print(validation_error.errors())