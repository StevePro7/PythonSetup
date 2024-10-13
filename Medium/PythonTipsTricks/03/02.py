import os
from pydantic_settings import BaseSettings

# Define the environment variables.
# You can also place them in a .env file or by using the export command to
# set them directly.
os.environ['DATABASE_URI'] = "file:memdb1?mode=memory&cache=shared"
os.environ['DEBUG_MODE'] = "True"


class Settings(BaseSettings):
    database_uri: str
    debug_mode: bool = False

    class Config:
        env_file = ".env" # Load settings from an optional .env file


# Instantiate and use the settings
settings = Settings()

print(settings.database_uri)
print(settings.debug_mode)
