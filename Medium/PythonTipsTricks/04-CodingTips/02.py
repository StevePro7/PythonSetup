# 02. Dictionary comprehensions
squares_dict = {}
for x in range(10):
    squares_dict[x] = x ** 2
print(squares_dict)


squares_dict2 = {x: x ** 2 for x in range(10)}
print(squares_dict2)

print(squares_dict == squares_dict2)