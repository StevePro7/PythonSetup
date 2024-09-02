from pydantic import BaseModel, ConfigDict, AliasGenerator, AliasPath


aliases = {
    "first_name": AliasPath("name", "first_name"),
    "last_name": AliasPath("name",  "last_name")
}


class FirstNameChoices(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: aliases.get(field_name, None)
        )
    )
    title: str
    first_name: str
    last_name: str


obj = FirstNameChoices(**{"name":{"first_name": "marc", "last_name": "Nealer"},"title":"Master Of All"})
print(obj)

# OUTPUT
# title='Master Of All' first_name='marc' last_name='Nealer'