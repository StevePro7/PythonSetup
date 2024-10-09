class Auth:
    def __init__(self, level="user"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args):
            if self.level == "admin":
                return func(args)
            else:
                raise Exception(f"Not allowed: '{self.level}")

        return wrapper


@Auth("admin")
def greet(name: str) -> str:
    test = f"Welcome! {name}"
    return test


name: str = "suzanne"
result = greet(name)
print(result)
