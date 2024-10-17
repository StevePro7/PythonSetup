import pytest
from typing import Generator

@pytest.fixture
def test_data() -> dict:
    with open("test_data.json", "r") as f:
        return json.load(f)


def test_data_processing(test_data) -> None:
    result = process_data(test_data["input"])
    assert result == test_data["expected_output"]