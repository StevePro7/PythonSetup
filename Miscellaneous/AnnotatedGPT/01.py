from typing import Annotated


def process_age(age: Annotated[int, "Age in years"]) -> str:
    return f"Processing age: {age}"


print(process_age(45))