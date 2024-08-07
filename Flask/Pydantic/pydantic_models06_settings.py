# Using Validation Decorators to Validate Functions
from pydantic import HttpUrl, Field
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    database_host = HttpUrl
    database_user: str = Field(min_length=5)
    database_password: str = Field(min_length=20)
    api_key: str = Field(min_length=20)


# from settings_management import AppConfig
# pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig