import inspect
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable)


def validate_function_arguments(func: F) -> F:
    def wrapper(*args, **kwargs):
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        type_annotations = {
            arg: param.annotation for arg, param in inspect.signature(func).parameters.items()
        }

        # validation process
        validation_errors = []
        for arg_name, expected_type in type_annotations.items():
            if expected_type is inspect._empty or expected_type is Any:
                continue

            actual_value = bound_args.arguments[arg_name]
            if not isinstance(actual_value, expected_type):
                validation_errors.append(
                    f"Invalid argument input for '{arg_name}': expected type {expected_type.__name__}, "
                    f"got {type(actual_value).__name__} instead"
                )

        if validation_errors:
            raise ValueError("\n".join(validation_errors))

        return func(*args, **kwargs)

    return cast(F, wrapper)


@validate_function_arguments
def process_user_data(user_id: int, name: str, tags: list = ["str"]) -> None:
    pass


# Example usage
try:
    process_user_data(123, "John Doe", ["customer", "premium"])  # Correct usage
    process_user_data("789", "Alice Brown")  # Invalid user_id type
except ValueError as e:
    print("Validation Error:", e)