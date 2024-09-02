A Practical Guide to using Pydantic
02-Sep-2024

https://medium.com/@marcnealer/a-practical-guide-to-using-pydantic-8aafa7feebf6


pip install -r requirements.txt
pip install --upgrade pip


Union[str, None]
OK if parameter is there or not

Optional[str]
expects parameter to be sent


DEFAULT values
list and dict
only one list object created and shared btwn all instances of this model

Field object
new instance being created for all instances of the model


Nested models


Field Validation
e.g.
Annotated validators
Ex03
decorator stating the fields to be applied to

not available in python3,8
ImportError: cannot import name 'Annotated' from 'typing' (/usr/lib/python3.8/typing.py)


BeforeValidator
validate data before default validation
chance to change and reformat the data 

also
AfterValidator
WrapValidator


BeforeValidator     transform incoming data
AfterValidator      check value is right type


NB: multiple values where one is optional
dob: Annotated[Annotated[datetime.datetime, BeforeValidator(stamp2date)] | None, Field(default=None)]


Model Validation
@model_validator(mode="after")
@model_validator(mode="before")

Alias
deal w/ incoming data and performing transformations

Validation alias
Serialization alias

define alias at model level instead of field level


AliasChoices
allows you to define a list of incoming value names
that will match a given field

key     field name
value   AliasChoices object


AliasPath
when incoming data is not flat or is blobs of json then
they are turned into dictionaries and passed to the model

AliasPath=
set a field to a value that is in the dictionary


Using AliasPath and AliasChoices