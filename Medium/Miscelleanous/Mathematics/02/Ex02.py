# --- Convex: f(x, y) = x^2 + y^2 ---
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Grid
xs = np.linspace(-3, 3, 200)
ys = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(xs, ys)
Z = X**2 + Y**2

# 3D surface
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_title("Convex Surface: f(x,y) = x² + y²")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("f")
plt.show()

# 2D contour
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=20)
plt.clabel(CS, inline=True, fontsize=8)
plt.title("Convex Contours: single basin")
plt.xlabel("x"); plt.ylabel("y")
plt.axis("equal")
plt.show()

# Optional: gradient descent traces to show convergence to (0,0)
def grad(xy):
    x, y = xy
    return np.array([2*x, 2*y])

def gd(start, lr=0.2, steps=25):
    pts = [np.array(start)]
    for _ in range(steps):
        g = grad(pts[-1])
        pts.append(pts[-1] - lr*g)
    return np.array(pts)

starts = [(-2.5, 2.0), (2.5, -2.5), (2.0, 1.5), (-1.5, -1.5)]
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=20)
for s in starts:
    path = gd(s, lr=0.2, steps=25)
    plt.plot(path[:,0], path[:,1], marker="o", markersize=2)
plt.title("Gradient Descent Paths on Convex Landscape")
plt.xlabel("x"); plt.ylabel("y")
plt.axis("equal")
plt.show()