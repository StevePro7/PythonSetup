Pydantic TypeAdapter: Supercharging Plain Python Types
15-Nov-2025

https://medium.com/@dynamicy/pydantic-typeadapter-supercharging-plain-python-types-d952623829c3

mkdir -p TypeAdapter
cd TypeAdapter
uv init --python 3.11.11
uv venv --python 3.11.11

source .venv/bin/activate
OR
.\.venv\Scripts\activate

uv add pydantic


TypeAdapter
give any Python type the same powers as BaseModel
validation, serialization, JSON schema
without forcing you to create a model class

e.g.
I want to validate is not a model class but a type expression

Type adapters provide a flexible way to perform validation and serialization based on a Python type. 

SUMMARY
BaseModel       class-centric
TypeAdapter     type-centric


IMPORTANT
TypeAdapter is not a a type
do not use TypeAdapter as a field annotation


CONCLUSION
TypeAdapter exists because real-world data isn't always a single model

real-world data is often:
- a nested list
- a dict of dicts
- a union of multiple shapes
- a structure defined by Annotated and constraints


TypeAdapter elevates these type expressions into powerful reusable validators


BaseModel
gives structure personality


TypeAdapter
gives types superpowers


Instead of this
class IntListWrapper(BaseModel):    
   items: list[int]
   
Try this
items = TypeAdapter(list[User]).validate_python(raw)