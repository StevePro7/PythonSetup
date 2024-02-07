#raise to power
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)

    return raise_to_exp


def different(x, exp):
    return pow(x, exp)

if __name__ == '__main__':
    print('beg')
    r = raise_to(2)
    s = r(3)
    print("3 * 3 = ", s)

    x = different(3, 2)
    print("3 * 3 = ", x)
    print('end')
