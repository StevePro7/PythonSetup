def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print("handled IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except KeyError:
        print("handled KeyError")


if __name__ == '__main__':
    lookups()