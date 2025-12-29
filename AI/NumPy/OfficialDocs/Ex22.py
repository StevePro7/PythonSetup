import numpy as np

# Array attributes
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.ndim)
# 2

print(a.shape)
# (3, 4)

print(a.size)
# 12
import math
b: bool = a.size == math.prod(a.shape)
print(b)
# True

c = a.dtype
print(c)
# int64

