import contextlib


@contextlib.contextmanager
def nest_test1(name: str):
    print(f"Entering: {name}")
    yield
    print(f"Exiting : {name}")


@contextlib.contextmanager
def nest_test2(name: str):
    print(f"Entering: {name}")
    yield name
    print(f"Exiting : {name}")
