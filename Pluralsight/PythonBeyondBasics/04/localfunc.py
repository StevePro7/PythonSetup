# local func

g = 'global'
def outer(p='params'):
    l = 'local'

    def inner():
        print(g, p, l)

    return inner


if __name__ == '__main__':
    print('beg')
    o = outer('test')
    r = o()
    print(r)
    print('end')
