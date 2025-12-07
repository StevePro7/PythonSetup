import numpy as np
import matplotlib.pyplot as plt

# Function: f(x) = x^3
x = np.linspace(-3, 3, 400)
f = x**3

# First derivative (velocity)
f_prime = 3*x**2

# Second derivative (acceleration)
f_double_prime = 6*x

# Plot function
plt.figure(figsize=(8,6))
plt.plot(x, f, label="$f(x) = x^3$", color="blue")

# Mark points for explanation
points = [-2, 0, 2]
for p in points:
    plt.scatter(p, p**3, color="red", s=60)
    plt.text(p, p**3+2, f"x={p}", ha="center", fontsize=9, color="red")

plt.title("Function, Velocity (slope), and Acceleration (curvature) Analogy")
plt.xlabel("x")
plt.ylabel("f(x)")

# Show slope (velocity) as tangent arrows and acceleration
for p in points:
    slope = 3*p**2
    acc = 6*p
    # Tangent arrow (velocity)
    dx = 0.5
    dy = slope*dx
    plt.arrow(p, p**3, dx, dy, head_width=0.15, head_length=0.3, fc='green', ec='green')
    # Label velocity
    plt.text(p+dx, p**3+dy, "vel", color="green")
    # Acceleration arrow (vertical, showing curvature direction)
    plt.arrow(p, p**3, 0, 0.8*np.sign(acc), head_width=0.15, head_length=0.3, fc='orange', ec='orange')
    plt.text(p, p**3+0.8*np.sign(acc)+0.3, "acc", color="orange", ha="center")

plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.legend()
plt.grid(True)
plt.show()