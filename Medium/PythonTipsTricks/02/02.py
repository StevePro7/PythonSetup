import pytest

params = [
	(1, 2, 3),
	(2, 4, 6),
	pytest.param(6, 9, 16, marks=pytest.mark.xfail)
]

@pytest.mark.parametrize("p1, p2, expected", params)
def test_func(p1, p2, expected):
	assert p1 + p2 == expected
