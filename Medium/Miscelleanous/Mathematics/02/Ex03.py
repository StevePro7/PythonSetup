# --- Saddle: f(x, y) = x^2 - y^2 ---
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

xs = np.linspace(-3, 3, 300)
ys = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(xs, ys)
Z = X**2 - Y**2

# 3D surface
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_title("Saddle Surface: f(x,y) = x² - y²")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("f")
plt.show()

# 2D contour
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=30)
plt.clabel(CS, inline=True, fontsize=8)
plt.title("Saddle Contours: ascent in one direction, descent in another")
plt.xlabel("x"); plt.ylabel("y")
plt.axis("equal")
plt.show()