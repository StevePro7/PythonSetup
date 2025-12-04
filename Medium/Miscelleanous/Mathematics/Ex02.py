import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)
tanh = np.tanh(x)
plt.plot(x, tanh); plt.title("Tanh"); plt.grid(); plt.show()