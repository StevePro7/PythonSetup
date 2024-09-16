import matplotlib.pyplot as plt
import numpy as np

# Span of Two Vectors
v1 = np.array([1, 2])
v2 = np.array([-1, 2])

# Generate Span
for a in np.arange(-2, 2, 0.5):
    for b in np.arange(-2, 2, 0.5):
        v = a*v1 + b*v2
        plt.plot(v[0], v[1], 'o', color='purple')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.show()
