import numpy as np
from scipy.linalg import null_space
from func import print_matrix


# Define the matrix
A = np.array([[1, 2], [2, 4]])

# Compute the null space of the matrix
N = null_space(A)

print_matrix(A)
print_matrix(N)