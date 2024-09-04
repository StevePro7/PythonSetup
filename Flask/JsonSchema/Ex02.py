from marshmallow import Schema, fields, post_load

class MyCustomClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"MyCustomClass(name={self.name}, age={self.age})"

class MyCustomClassSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)

    @post_load
    def make_custom_class(self, data, **kwargs):
        return MyCustomClass(**data)

json_str = '{"name": "John Doe", "age": 30}'

schema = MyCustomClassSchema()
result = schema.loads(json_str)

print(result)  # Output: MyCustomClass(name=John Doe, age=30)
