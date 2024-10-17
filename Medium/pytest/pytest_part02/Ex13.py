import pytest


@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4), (3, 6)])
def test_double(input, expected) -> None:
    assert input * 2 == expected



# Multiple args
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (3, 5, 8)
    ]
)
def test_add(x, y, expected) -> None:
    assert x + y == expected