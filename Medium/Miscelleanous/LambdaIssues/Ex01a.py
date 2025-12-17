callbacks = []
for i in range(5):
    callbacks.append(lambda : i)

for func in callbacks:
    print(func())

# 4
# 4
# 4
# 4
# 4