# --- Non-convex: Himmelblau's function ---
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def f_h(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

xs = np.linspace(-6, 6, 400)
ys = np.linspace(-6, 6, 400)
X, Y = np.meshgrid(xs, ys)
Z = f_h(X, Y)

# 3D surface
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_title("Non-Convex Surface: Himmelblau's Function")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("f")
plt.show()

# 2D contour
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=50)
plt.clabel(CS, inline=True, fontsize=7)
plt.title("Non-Convex Contours: multiple basins")
plt.xlabel("x"); plt.ylabel("y")
plt.axis("equal")
plt.show()

# Optional: gradient descent traces from different inits (may land in different minima)
def grad_h(xy):
    x, y = xy
    # Analytical gradient
    gx = 4*x*(x**2 + y - 11) + 2*(x + y**2 - 7)
    gy = 2*(x**2 + y - 11) + 4*y*(x + y**2 - 7)
    return np.array([gx, gy])

def gd_h(start, lr=0.01, steps=200):
    pts = [np.array(start, dtype=float)]
    for _ in range(steps):
        g = grad_h(pts[-1])
        pts.append(pts[-1] - lr*g)
    return np.array(pts)

starts = [(-4, 4), (-4, -4), (0, 0), (4, 4), (4, -4)]
plt.figure(figsize=(6,5))
CS = plt.contour(X, Y, Z, levels=50)
for s in starts:
    path = gd_h(s, lr=0.01, steps=300)
    plt.plot(path[:,0], path[:,1], marker="o", markersize=2)
plt.title("Gradient Descent Paths on Non-Convex Landscape (Himmelblau)")
plt.xlabel("x"); plt.ylabel("y")
plt.axis("equal")
plt.show()