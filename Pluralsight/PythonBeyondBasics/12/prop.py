import contextlib


@contextlib.contextmanager
def propagater(name: str, propagate: bool):
    try:
        yield
        print(f"Name: '{name}' exited normally")
    except Exception:
        print(f"Name: '{name}' received an exception!")
        if propagate:
            raise
