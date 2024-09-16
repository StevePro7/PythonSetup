import numpy as np


# Singular Matrix
A = np.array([[1, 2], [2, 4]])  # This matrix is singular

# Attempt to compute its inverse (will raise an error)
try:
    np.linalg.inv(A)
except np.linalg.LinAlgError:
    print("Matrix is singular, cannot find its inverse.")