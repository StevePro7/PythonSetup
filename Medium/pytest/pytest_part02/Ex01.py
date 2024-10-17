import pytest


def test_raises() -> None:
    with pytest.raises(ValueError):
        raise ValueError("Invalid value")