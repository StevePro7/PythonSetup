import numpy as np


# Determinant of a Matrix
A = np.array([[1, 2], [3, 4]])
det_A = np.linalg.det(A)

# No direct visualization for determinant
print("Determinant of A:", round(det_A, 2))
