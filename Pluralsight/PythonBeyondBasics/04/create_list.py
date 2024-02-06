# create list

def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            bob = args[index]
            if bob < 0:
                raise ValueError("'Argument {} must be non-negative [where value = '{}']".format(index, bob))
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


if __name__ == '__main__':
    print('beg')
    v = [-1, 2, 3]
    S = -1
    x = create_list(v, S)
    print(x)
    print('end')
