import numpy as np

# Basic array operations
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
# [2 3]

print(data - ones)
# [0 1]

print(data * data)
# [1 4]

print(data / data)
# [1. 1.]


a = np.array([1, 2, 3, 4])
print(a.sum())
# 10

b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))
# sum on the cols
# [3 3]

print(b.sum(axis=1))
# sum on the rows
# [2 4]