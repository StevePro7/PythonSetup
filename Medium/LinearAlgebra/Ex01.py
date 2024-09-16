import matplotlib.pyplot as plt
import numpy as np

# Vector
v = np.array([2, 3])

# Plot
plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="r")
plt.xlim(-2, 5)
plt.ylim(-2, 5)
plt.grid()
plt.show()
