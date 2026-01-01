import numpy as np

# Generating random numbers
rng = np.random.default_rng()

a = rng.integers(5, size= (2, 4))
print(a)
# [[4 4 1 3]
#  [3 3 4 0]]


# How to get unique items and counts
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
b = np.unique(a)
print(b)
# [11 12 13 14 15 16 17 18 19 20]


unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)
# [ 0  2  3  4  5  6  7 12 13 14]


a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_values = np.unique(a_2d)
print(unique_values)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]


unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]


unique_rows, indices, occurences_count = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(indices)
# [0 1 2]
print(occurences_count)
# [2 1 1]