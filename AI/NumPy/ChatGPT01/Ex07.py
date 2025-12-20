# Ex07        Broadcasting (VERY IMPORTANT)
import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6]])
#print(x)
#[[1 2 3]
# [4 5 6]]

y = np.array([10, 20, 30])
#print(y)
# [10 20 30]

z = x + y
print(z)
#[[11 22 33]
# [14 25 36]]