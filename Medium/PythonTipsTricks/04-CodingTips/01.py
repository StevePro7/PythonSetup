# 01. List comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
print()

# Condensed way: using list comprehensions
squares2 = [x ** 2 for x in range(10)]
print(squares2)

print(squares == squares2)