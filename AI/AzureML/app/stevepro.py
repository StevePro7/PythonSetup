import json
from app.application import Application
from app.providers.app_provider import AppProvider

def init():
    app_provider: AppProvider = AppProvider()
    app_provider.get_app()


def run(raw_data: str) -> dict:
    app_provider: AppProvider = AppProvider()
    app: Application = app_provider.get_app()
    response: dict = app.handle(raw_data)
    return response


init()

raw_data: str = '{"data": "bar"}'
response = run(raw_data)

print(response)