import pytest
from Engine.FooManager import bar

def test_bar():
    ex = 7
    ac = bar()
    assert ex == ac
