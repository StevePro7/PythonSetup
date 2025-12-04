import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define function
def f(x, y):
    return x**2 + x*y + y**2

# Grid
xs = np.linspace(-3, 3, 100)
ys = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xs, ys)
Z = f(X, Y)

# 3D surface
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
ax.set_title("Convex Surface with Positive Definite Hessian")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")
plt.show()

# Contour
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.clabel(CS, inline=True, fontsize=8)
plt.title("Contour Lines Showing Convex Shape")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()