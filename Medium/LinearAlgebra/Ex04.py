import matplotlib.pyplot as plt
import numpy as np

# Linearly Independent Vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Plot
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid()
plt.show()
