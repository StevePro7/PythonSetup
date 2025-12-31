from logging import info

import numpy as np

# Creating matrices
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
# [[1 2]
#  [3 4]
#  # [5 6]]

print(data[0, 1])
# 2

print(data[1:3])
# [[3 4]
#  [5 6]]

print(data[0:2, 0])
# [1 3]


print(data.max())
# 6

print(data.min())
# 1

print(data.sum())
# 21


data = np.array([[1, 2], [5, 3], [4, 6]])
print(data)
# [[1 2]
#  [5 3]
#  [4 6]]

print(data.max(axis=0))
# [5 6]

print(data.max(axis=1))
# [2 5 6]


data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(data + ones)
# [[2 3]
#  [4 5]]

data = np.array([[1, 2], [3, 4], [5, 6]])
ones = np.array([[1, 1]])
print(data + ones)
# [[2 3]
#  [4 5]
#  [6 7]]

print(np.ones((4, 3, 2)))
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]

print(np.ones(3))
# [1. 1. 1.]
print(np.zeros(3))
# [0. 0. 0.]

rng = np.random.default_rng()
print(rng.random(3))
# [0.06607687 0.79856254 0.10839766]


print(np.ones((3, 2)))
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

print(np.zeros((3, 2)))
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

print(rng.random((3, 2)))
# [[0.32948319 0.24874326]
#  [0.96875916 0.6592108 ]
#  [0.36708762 0.26853433]]