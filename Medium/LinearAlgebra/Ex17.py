import matplotlib.pyplot as plt
import numpy as np


# Scalar Multiplication of a Vector
scalar = 3
v = np.array([1, 2])
v_scaled = scalar * v

# Plot
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='Original')
plt.quiver(0, 0, v_scaled[0], v_scaled[1], angles='xy', scale_units='xy', scale=1, color='b', label='Scaled')
plt.xlim(-1, 6)
plt.ylim(-1, 8)
plt.grid()
plt.legend()
plt.show()
