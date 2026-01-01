from logging import info

import numpy as np

# Transposing and reshaping a matrix
# data.reshape(2, 3)
# data.reshape(3, 2)

arr = np.arange(6).reshape(2,3)
print(arr)
# [[0 1 2]
#  [3 4 5]]

b = arr.transpose()
print(b)
# [[0 3]
#  [1 4]
#  [2 5]]