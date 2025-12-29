import numpy as np

# Reading the example code
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)
# (2, 3)


a = np.array([10, 2, 3, 4 ,5, 6])
print(a[:3])
# [10  2  3]

b = a[3:]
print(b)
# [4 5 6]

b[0] = 40
print(a)
# [10  2  3 40  5  6]


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a[1, 3])
# 8
