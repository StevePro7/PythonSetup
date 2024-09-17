import matplotlib.pyplot as plt
import numpy as np

from func import print_matrix

# Eigenvectors and Eigenvalues
A = np.array([[1, 2], [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print_matrix(A)

# Plotting
fig, ax = plt.subplots()

# Origin
origin = [0, 0]

# Plot each eigenvector
for i in range(len(eigenvalues)):
    ax.quiver(
        *origin,
        eigenvectors[0, i],
        eigenvectors[1, i],
        scale=3,
        scale_units="xy",
        angles="xy",
    )

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Eigenvectors of A")

plt.show()
