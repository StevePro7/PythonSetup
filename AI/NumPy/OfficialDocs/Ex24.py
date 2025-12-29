import numpy as np

# Adding removing and sorting elements
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
b = np.sort(arr)
print(b)
# [1 2 3 4 5 6 7 8]


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
print(c)
# [1 2 3 4 5 6 7 8]


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y))
print(z)
# [[1 2]
#  [3 4]
#  [5 6]]



