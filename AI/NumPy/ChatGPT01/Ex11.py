# Ex11        Dot Product & Norms
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# dot product
z = x @ y
print(z)
# 32

w = np.linalg.norm(x)
print(w)
# 3.7416573867739413