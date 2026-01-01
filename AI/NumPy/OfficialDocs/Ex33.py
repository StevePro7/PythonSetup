import numpy as np

# Reshaping and flattening multidimensional arrays
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x.flatten())
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

a1  = x.flatten()
a1[0] = 99
print(x)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a1)
# [99  2  3  4  5  6  7  8  9 10 11 12]