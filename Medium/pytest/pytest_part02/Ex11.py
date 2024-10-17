import pytest
from typing import Generator

@pytest.fixture
def app_config() -> dict:
    return {
        "API_URL": "https://api.example.com",
        "MAX_RETRIES": 3,
        "TIMEOUT": 30
    }


def test_api_connection(app_config) -> None:
    client = APIClient(app_config["API_URL"])
    assert client.max_retries == app_config["MAX_RETRIES"]
    assert client.timeout == app_config["TIMEOUT"]