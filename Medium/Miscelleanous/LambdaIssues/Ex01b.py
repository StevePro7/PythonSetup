funcs = [lambda: i for i in range(5)]
print([f() for f in funcs])

# [4, 4, 4, 4, 4]
