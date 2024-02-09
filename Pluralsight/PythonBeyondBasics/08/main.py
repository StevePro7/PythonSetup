# driver program
from tracer import Trace


def main():
    result = map(Trace()(ord), 'The quick brown fox')
    print(result)


if __name__ == '__main__':
    main()
