import pytest


@pytest.fixture
def sample_data() -> dict:
    return {"name": "John Doe", "age": 30}


def test_sample_data(sample_data) -> None:
    assert sample_data["name"] == "John Doe"
    assert sample_data["age"] == 30