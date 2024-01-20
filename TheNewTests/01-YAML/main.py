""" hello docstring """
import sys


def main():
    """ hello docstring """
    print("main beg")

    coll = sys.argv[1:]
    for x in coll:
        print(x)

    print("main end")


if __name__ == '__main__':
    main()
