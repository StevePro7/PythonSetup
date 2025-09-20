import numpy as np
import matplotlib.pyplot as plt

# Points (square)
points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

# Transformation matrix: rotate 90 degrees
rotation = np.array([[0, -1],
                     [1, 0]])

# Apply transformation
rotated = np.dot(points, rotation.T)

# Plot
plt.scatter(points[:, 0], points[:, 1], color = "blue", label="Original")
plt.scatter(rotated[:, 0], rotated[:, 1], color = "red", label="Rotated")
plt.legend()
plt.show()