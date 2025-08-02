import uuid
from functools import lru_cache

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ADMIN_API_KEY: uuid.UUID = Field(
        ...,
        description="The API key for the admin user.",
        title="Admin API Key",
        examples=["123e4567-e89b-12d3-a456-426614174000"],
    )
    #
    # AWS_ACCOUNT_ID: str = Field(
    #     ...,
    #     description="The AWS account ID.",
    #     title="AWS Account ID",
    #     examples=["123456789012"],
    # )
    #
    # AWS_ACCESS_KEY_ID: str = Field(
    #     ...,
    #     description="The AWS access key ID.",
    #     title="AWS Access Key ID",
    # )
    #
    # AWS_SECRET_ACCESS_KEY: str = Field(
    #     ...,
    #     description="The AWS secret access key.",
    #     title="AWS Secret Access Key",
    # )
    #
    # AWS_REGION: str = Field(
    #     ...,
    #     description="The AWS region.",
    #     title="AWS Region",
    #     examples=["us-east-1"],
    # )

    BASE_URL: HttpUrl = Field(
        ...,
        description="The base URL of the API.",
        title="Base URL",
        examples=["http://localhost:3000"],
    )

    PG_CONNECTION_STRING: str = Field(
        ...,
        description="The PostgreSQL connection URL.",
        title="PostgreSQL Connection String",
        examples=["postgresql://user:password@localhost/db"],
    )

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
