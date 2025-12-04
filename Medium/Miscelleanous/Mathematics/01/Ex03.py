import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)
relu = np.maximum(0, x)
plt.plot(x, relu); plt.title("ReLU"); plt.grid(); plt.show()
