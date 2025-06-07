# driver program
from point import Point2D
from table import Table


def main():
    p = Point2D(123, 456)
    print(f"circle at {str(p)}")
    print(f"circle at {repr(p)}")
    print(f"{Point2D(1, 2)}")
    print(f"{Point2D(1, 2):r}")

    table = Table(['First name', 'Last name'],
                  ['Fred', 'George', 'Scooby'],
                  ['Flintsone', 'Jetson', 'Doo'])
    print(repr(table))
    print()
    print(str(table))


if __name__ == '__main__':
    main()
