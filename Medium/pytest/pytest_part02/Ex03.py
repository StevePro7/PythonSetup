import pytest


@pytest.fixture(scope="module")
def expensive_computation() -> Any:
    result = perform_expensive_computation()
    return result


def test_first(expensive_computation) -> None:
    assert expensive_computation > 0


def test_second(expensive_computation) -> None:
    assert expensive_computation < 100