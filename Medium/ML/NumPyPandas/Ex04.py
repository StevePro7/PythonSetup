# Vectorized Operations — NumPy’s Real Magic
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
d = a * b
e = np.sqrt(a)

print(c)        # [5 7 9]
print(d)        # [4 10 18]
print(e)        # [1.         1.41421356 1.73205081]

