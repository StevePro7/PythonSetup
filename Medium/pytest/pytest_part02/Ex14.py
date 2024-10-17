import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(1, 2, id="small number"),
        pytest.param(100, 200, id="large number"),
        pytest.param(-1, -2, id="negative number"),
    ]
)
def test_double(input, expected) -> None:
    assert input * 2 == expected



# Multiple parametrize decorators
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_multiply(x, y) -> None:
    assert x * y < 10