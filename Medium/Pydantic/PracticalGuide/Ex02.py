from pydantic import BaseModel, Field


# Default
class DefaultsModel(BaseModel):
    first_name: str = "jane"
    middle_names: list = Field(default_factory=list)
    last_name: str = "doe"


# Nested
class NameModel(BaseModel):
    first_name: str
    last_name: str


class UserModel(BaseModel):
    username: str
    name: NameModel
