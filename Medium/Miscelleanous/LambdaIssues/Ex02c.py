def make_func(x):
    return lambda: x

funcs = [make_func(i) for i in range(5)]
print([f() for f in funcs])  # [0, 1, 2, 3, 4]