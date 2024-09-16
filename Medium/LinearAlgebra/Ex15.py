import numpy as np
from func import print_matrix


# Rank 1 Matrix
A_rank1 = np.array([[1, 2], [1, 2]])

# Rank 2 Matrix
A_rank2 = np.array([[1, 2], [3, 4]])

# Rank 3 Matrix (must be at least 3x3)
A_rank3 = np.array([[1, 0, 2], [0, 1, 3], [1, 1, 5]])

matrices = [A_rank1, A_rank2, A_rank3]
for matrix in matrices:
    print_matrix(matrix)
    print(f"Rank: {np.linalg.matrix_rank(matrix)}\n")
