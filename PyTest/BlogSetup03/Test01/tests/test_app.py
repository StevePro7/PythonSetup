import pytest
from src.app import foo
from src.app import hello

def test_foo():
    ex = 7
    ac = foo()
    assert ex == ac


def test_hello(steve_fixture):
    ex = steve_fixture
    ac = hello()
    assert ex == ac


def test_user_creds(user_creds):
    assert user_creds("John", "john@host.com") == {
        "name": "John",
        "email": "john@host.com",
    }
