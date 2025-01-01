# 2. Numpy
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))

# Operations
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_std = np.std(arr)

# Indexing
slice_arr = arr[1:3]
print(slice_arr)