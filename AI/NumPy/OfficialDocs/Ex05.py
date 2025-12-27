import numpy as np

# Universal functions
B = np.arange(3)
print(B)
# [0 1 2]

print(np.exp(B))
# [1.         2.71828183 7.3890561 ]

print(np.sqrt(B))
# [0.         1.         1.41421356]

C = np.array([2., -1., 4.])
print(C)
print(C.dtype.name)
# float64

print(np.add(B, C))
# [0 1 2]
# [2. -1.  4.]
# [2. 0. 6.]
