def foo() -> int:
    return 7


def test_foo() -> None:
    ex = 8
    ac = 7
    assert ex == ac
