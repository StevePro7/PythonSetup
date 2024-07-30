Pydantic
30-Jul-2024

Pydantic: Simplifying Data Validation in Python
https://realpython.com/python-pydantic

Python’s Pydantic Library
Pydantic is a powerful data validation and settings management library for Python

Installing Pydantic
pip install pydantic
pip install pydantic[email]
pip install pydantic-settings

Using Models
Pydantic’s primary way of defining data schemas is through models. A Pydantic model is an object, similar to a Python dataclass, that defines and stores data about an entity with annotated fields. Unlike dataclasses, Pydantic’s focus is centered around automatic data parsing, validation, and serialization.

main01.py

main02.py
pprint()
https://docs.python.org/3/library/pprint.html

You can convert your JSON schema to a JSON string using json.dumps(),


Using Fields for Customization and Metadata
The Field class allows you to customize and add metadata to your model’s fields. To see how this works, take a look at this example:

main20.py
pydantic_core._pydantic_core.ValidationError: 3 validation errors for Employee
name