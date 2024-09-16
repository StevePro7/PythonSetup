import numpy as np

from func import print_matrix

# Inverse of a Matrix
A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)

print("original matrix")
print_matrix(A)

print("After inverse")
print_matrix(A_inv)
