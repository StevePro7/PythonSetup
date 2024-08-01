import pytest


@pytest.mark.great
def test_steven():
    num = 100
    assert num > 90


@pytest.mark.great
def test_steven_equal():
    num = 100
    assert num >= 100


@pytest.mark.other
def test_steven_less():
    num = 100
    assert num < 200
