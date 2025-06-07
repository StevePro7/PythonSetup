import contextlib
import sys

class LoggingContextManager1:

    def __enter__(self):
        print(f"LoggingContextManager.__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"LoggingContextManager.__exit__({exc_type}, {exc_val}, {exc_tb})")
        return


class LoggingContextManager2:

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"LoggingContextManager.__exit__() normal exit")
        else:
            print(f"LoggingContextManager.__exit__({exc_type}, {exc_val}, {exc_tb})")


@contextlib.contextmanager
def logging_context_manager3():
    print("logging_context_manager.__enter__()")
    try:
        yield "You are in a with-block"
        print("logging_context_manager.__exit__() normal exit")
    except Exception:
        print("logging_context_manager.__exit__() exceptional exit")
        sys.exc_info()          # Exception not propagated


@contextlib.contextmanager
def logging_context_manager4():
    print("logging_context_manager.__enter__()")
    try:
        yield "You are in a with-block"
        print("logging_context_manager.__exit__() normal exit")
    except Exception:
        print("logging_context_manager.__exit__() exceptional exit")
        sys.exc_info()          # Exception IS propagated
        raise
