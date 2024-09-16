import matplotlib.pyplot as plt
import numpy as np

# Vector
v = np.array([2, 3])

# Calculate the unit vector
unit_vector = v / np.linalg.norm(v)

# Plot
plt.quiver(0, 0, unit_vector[0], unit_vector[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.grid()
plt.show()
