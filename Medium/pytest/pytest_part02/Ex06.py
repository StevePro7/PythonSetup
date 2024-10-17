import pytest


@pytest.fixture
def fruit(request) -> Any:
    return request.param


@pytest.mark.parametrize("fruit", ["apple", "banana", "orange"])
def test_fruit(fruit) -> None:
    assert len(fruit) > 3