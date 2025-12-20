# Ex14        Softmax
import numpy as np

x = np.array([1.0, 2.0, 3.0])

exp = np.exp(x - x.max())
print(exp)
# [0.13533528 0.36787944 1.        ]

softmax = exp / exp.sum()
print(softmax)
# [0.09003057 0.24472847 0.66524096]