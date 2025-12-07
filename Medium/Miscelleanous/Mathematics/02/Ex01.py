import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 200)
f_convex = x**2
f_nonconvex = np.sin(2*x) + 0.3*x
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x, f_convex, label="Convex: $x^2$")
plt.fill_between(x, f_convex, np.maximum(f_convex[50], f_convex[150]), alpha=0.1)
plt.title("Convex Function")
plt.grid(); plt.legend()
plt.subplot(1,2,2)
plt.plot(x, f_nonconvex, label="Non-Convex: $\sin(2x)+0.3x$")
plt.title("Non-Convex Function")
plt.grid(); plt.legend()
plt.show()