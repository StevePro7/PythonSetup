import numpy as np
from scipy.linalg import null_space
from func import print_matrix


# Dot Product of Two Vectors
v1 = np.array([1, 2])
v2 = np.array([2, 3])
dot_product = np.dot(v1, v2)

# No direct visualization for dot product
print("Dot Product:", dot_product)
