# closures
def outer():
    x = 3

    def inner(y):
        return x + y

    return inner


def enclosing():
    x = 'closed over'

    def local_func():
        print(x)

    return local_func


if __name__ == '__main__':
    print('beg')
    o = outer()
    z = o(2)
    print(z)

    e = enclosing()
    e()
    print('end')
