#escape unicade
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def north_city():
    return 'Chè'

if __name__ == '__main__':
    print('beg')
    c = north_city()
    print(c)
    print('end')
