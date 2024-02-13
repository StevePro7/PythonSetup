from typing import List


def doit_args(*args: int) -> None:
    print(id(args))
    for arg in args:
        print(f"yeah:{arg}")

def doit_kwargs(**kwargs: dict) -> None:
    print(id(kwargs))
    for k in kwargs.keys():
        print(f"yeah:{k}")

    for v in kwargs.values():
        print(f"yeah:{v}")


def main():
    print("beg")

    args = {4, 2, 3, 3, 2}
    print(id(args))
    doit_args(*args)

    kwargs = {"x": 1, "y": 2}
    print(id(args))
    doit_kwargs(**kwargs)

    print("end")


if __name__ == '__main__':
    main()