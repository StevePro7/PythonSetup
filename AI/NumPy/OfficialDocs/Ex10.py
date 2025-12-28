import numpy as np

# Indexing with boolean arrays
a = np.arange(12).reshape(3,4)
b = a > 4       # `b` is a boolean with `a`'s shape
print(b)
# [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

print(a[b])
# [ 5  6  7  8  9 10 11]

a[b] = 0        # All elements of `a` higher than 4 become 0
print(a)
# [[0 1 2 3]
#  [4 0 0 0]
#  [0 0 0 0]]
