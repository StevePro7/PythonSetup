from pydantic import TypeAdapter

schema = TypeAdapter(list[int]).json_schema()
print(schema)