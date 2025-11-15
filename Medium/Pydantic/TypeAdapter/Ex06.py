from typing import List
from typing_extensions import TypedDict
from pydantic import TypeAdapter, ValidationError

class Task(TypedDict):
    id: int
    name: str

adapter = TypeAdapter(List[Task])

class InvalidTaskList(Exception):
    pass

def process_tasks(raw):
    try:
        return adapter.validate_python(raw)
    except ValidationError as e:
        raise InvalidTaskList(str(e)) from e