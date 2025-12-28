import numpy as np

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])          # 1st  dim selection
b2 = np.array([True, False, True, False])   # 2nd dim selection

print(a[b1, :])                             # selecting rows
# row 1 + 2
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[b1])                                # same thing
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:, b2])                             # selecting columns
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]

print(a[b1, b2])                            # a weird thing to do
# [ 4 10]