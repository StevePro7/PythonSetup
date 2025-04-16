funcs = [lambda x: x + i for i in range(3)]
print([f(10) for f in funcs])  # [12, 12, 12] (Unexpected!)


funcs_fix = [lambda x, i=i: x + i for i in range(3)]
print([f(10) for f in funcs_fix])  # [12, 12, 12] (Unexpected!)