matrix = [[j for j in range(5)] for i in range(3)]
# print(matrix)
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


filtered = [x for x in range(10) if x % 2 == 0]
# print(filtered)
# [0, 2, 4, 6, 8]


pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(pairs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


square = lambda x: x ** 2
# print(square(5))
# 25


squared = [(lambda x: x**2)(x) for x in range(5)]
# print(squared)
# [0, 1, 4, 9, 16]


nested = [[1, 2, 3], [4, 5, 6], [6, 7]]
flattened = [x for sublist in nested for x in sublist]
# print(flattened)
# [1, 2, 3, 4, 5, 6, 6, 7]


import math
transformed = [math.sqrt(x) for x in range(1, 6)]
# print(transformed)
# [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]


mapped = list(map(lambda x: x**2, range(5)))
filtered = list(filter(lambda x: x > 5, mapped))
# print(mapped)
# print(filtered)
# [0, 1, 4, 9, 16]
# [9, 16]


conditional = [x if x > 2 else x**2 for x in range(5)]
# print(conditional)
# [0, 1, 4, 3, 4]


complex_transformation = list(map(lambda x: x**2 if x % 2 == 0 else x + 5, range(5)))
# print(complex_transformation)
# [0, 6, 4, 8, 16]