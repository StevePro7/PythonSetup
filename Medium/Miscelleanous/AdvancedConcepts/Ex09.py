# Nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)


# With conditions
squares = [x ** 2 for x in range(1) if x % 2 == 0]
print(squares)