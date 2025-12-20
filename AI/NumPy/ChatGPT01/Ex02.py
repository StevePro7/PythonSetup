# Ex02        Arrays (ndarray)
import numpy as np

# Arrays [ndarray]  ND = number dimensions
a = np.array([1, 2, 3])
print(type(a))          # numpy.ndarray
print(a.shape)          # (3, )
print(a.ndim)           # 1
print(type(a.shape))    # tuple
print()

b = np.array([[1, 2], [3, 4]])
print(type(b))          # numpy.ndarray
print(b.shape)          # (2, 2)
print(b.ndim)           # 2
print(type(b.shape))    # tuple
print()

print(a.dtype)          # int64
print(b.dtype)          # int64