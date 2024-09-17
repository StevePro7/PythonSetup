import matplotlib.pyplot as plt
import numpy as np

# Linear Transformation of a Square
T = np.array([[1, 2], [2, 1]])  # Transformation matrix
square = np.array([[0, 0, 1, 1, 0], [0, 1, 1, 0, 0]])  # Original square
transformed_square = np.dot(T, square)  # Apply transformation

# Plot Original and Transformed Square
plt.figure(figsize=(8, 4))

# Original Square
plt.subplot(1, 2, 1)
plt.plot(square[0], square[1], "o-", color="blue")
plt.title("Original Square")
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.axhline(0, color="grey", linewidth=0.5)
plt.axvline(0, color="grey", linewidth=0.5)
plt.grid(True)

# Transformed Square
plt.subplot(1, 2, 2)
plt.plot(transformed_square[0], transformed_square[1], "o-", color="red")
plt.title("Transformed Square")
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.axhline(0, color="grey", linewidth=0.5)
plt.axvline(0, color="grey", linewidth=0.5)
plt.grid(True)

plt.show()
