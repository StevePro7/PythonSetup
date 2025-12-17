from functools import partial

def return_value(x):
    return x

funcs = [partial(return_value, i) for i in range(5)]
print([f() for f in funcs])  # [0, 1, 2, 3, 4]