import numpy as np
import matplotlib.pyplot as plt

# Define function and gradient
def f(x, y):
    return x**2 + y**2

def grad_f(x, y):
    return np.array([2*x, 2*y])

# Grid for plotting
x_vals = np.linspace(-3, 3, 20)
y_vals = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

# Compute gradients
U, V = grad_f(X, Y)

plt.figure(figsize=(6,5))
plt.contour(X, Y, Z, levels=15, cmap='viridis')
plt.quiver(X, Y, U, V, color='red')  # Gradient arrows
plt.title("Gradient Vectors Point to Steepest Ascent")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axis("equal")
plt.show()