import pytest

def foo():
    return 7

def test_foo():
    ex = 9
    ac = foo()
    assert ex == ac
