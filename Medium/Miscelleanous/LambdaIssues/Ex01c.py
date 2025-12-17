funcs = []
for i in range(5):
    funcs.append(lambda: i)

print([f() for f in funcs])

# [4, 4, 4, 4, 4]
