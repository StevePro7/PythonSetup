# Ex09        Reshaping (Neural Net Backbone)
import numpy as np

x = np.arange(6)
print(x)
# [0 1 2 3 4 5]

a = x.reshape(2, 3)
print(a)
#[[0 1 2]
# [3 4 5]]

b = x.reshape(-1, 2)
print(b)
#[[0 1]
# [2 3]
# [4 5]]

c = x.flatten()
print(c)
# [0 1 2 3 4 5]