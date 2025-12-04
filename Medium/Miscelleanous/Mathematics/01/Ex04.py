import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)
alpha = 0.1
leaky_relu = np.where(x>0, x, alpha*x)
plt.plot(x, leaky_relu); plt.title("Leaky ReLU"); plt.grid(); plt.show()