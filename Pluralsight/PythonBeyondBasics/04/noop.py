#noop
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()

    return noop_wrapper


@noop
def hello():
    print("Hello world")

if __name__ == '__main__':
    print('beg')
    hello()
    print('end')
