import pytest
from typing import Callable

@pytest.fixture
def create_user() -> Callable:
    def _create_user(name, age) -> dict:
        return {"name": name, "age": age}
    return _create_user


def test_user_creation(create_user) -> None:
    user = create_user("Alice", 30)
    assert user["name"] == "Alice"
    assert user["age"] == 30
