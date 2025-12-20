# Ex12        Randomness
import numpy as np

np.random.seed(0)

a = np.random.randn(3)
print(a)
# [1.76405235 0.40015721 0.97873798]

b = np.random.choice([0, 1], size=10)
print(b)
# [1 1 1 0 0 1 0 0 0 0]