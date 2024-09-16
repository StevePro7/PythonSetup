import matplotlib.pyplot as plt
import numpy as np

# Vector
v = np.array([2, 3])

# Original square defined by its corners
square = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])

# Matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [0, 2]])

# Apply matrix A and B transformations
transformed_square_A = np.dot(A, square)
transformed_square_B = np.dot(B, square)

# Apply matrix A then B transformation (A x B)
transformed_square_AB = np.dot(A, transformed_square_B)

# Plotting
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

# Original Square
ax[0].plot(square[0], square[1], 'o-', color='grey')
ax[0].set_title('Original Square')
ax[0].set_xlim(-1, 5)
ax[0].set_ylim(-1, 5)

# Square after applying matrix A
ax[1].plot(transformed_square_A[0], transformed_square_A[1], 'o-', color='red')
ax[1].set_title('After applying A')
ax[1].set_xlim(-1, 5)
ax[1].set_ylim(-1, 5)

# Square after applying matrix B
ax[2].plot(transformed_square_B[0], transformed_square_B[1], 'o-', color='blue')
ax[2].set_title('After applying B')
ax[2].set_xlim(-1, 5)
ax[2].set_ylim(-1, 5)

# Square after applying matrix A then B
ax[3].plot(transformed_square_AB[0], transformed_square_AB[1], 'o-', color='green')
ax[3].set_title('After applying A x B')
ax[3].set_xlim(-1, 10)
ax[3].set_ylim(-1, 10)

plt.show()
