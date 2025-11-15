from pydantic import TypeAdapter

adapter = TypeAdapter(list[int])
result = adapter.validate_python(["1", 2, 3])
print(result)