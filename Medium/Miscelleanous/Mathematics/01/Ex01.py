import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)
sigmoid = 1/(1+np.exp(-x))
plt.plot(x, sigmoid); plt.title("Sigmoid"); plt.grid(); plt.show()
