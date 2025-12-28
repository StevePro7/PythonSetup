import numpy as np

# Advanced indexing and index tricks

## Indexing with array of indices
a = np.arange(12)**2  # the first 12 square numbers
print(a)
# [  0   1   4   9  16  25  36  49  64  81 100 121]

i = np.array([1, 1, 3, 8, 5])  # an array of indices
print(i)
# [1 1 3 8 5]

print(a[i])         # the elements of `a` at the positions `i`
# [ 1  1  9 64 25]

j = np.array([[3, 4], [9, 7]])      # a bidimensional array of indices
print(j)
# [[3 4]
#  [9 7]]

print(a[j])
# [[ 9 16]
#  [81 49]]


palette = np.array([[0, 0, 0],          # black
                    [255, 0, 0],        # red
                    [0, 255, 0],        # green
                    [0, 0, 255],        # blue
                    [255, 255, 255]])   # white
image = np.array([[0, 1, 2, 0],         # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])

print(palette[image])                   # the (2, 4, 3) color image
# [[0   0   0]
#  [0   0 255]
# [255
# 255
# 255]
# [0   0   0]]]


a = np.arange(12).reshape((3, 4))
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

i = np.array([[0, 1],           # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],           # indices for the second dim
              [3, 3]])

print(a[i, j])                  # # i and j must have equal shape
# [[ 2  5]
#  [ 7 11]]
# 2 = [0, 2]
# 5 = [1, 1]
# 7 = [1, 2]
# 11= [2, 3]

print(a[i, 2])
# [[ 2  6]
#  [ 6 10]]

print(a[:, j])
# [[[ 2  1]
#   [ 3  3]]
#
#  [[ 6  5]
#   [ 7  7]]
#
#  [[10  9]
#   [11 11]]]


s = np.array([i, j])
# print(a[s])
# IndexError: index 3 is out of bounds for axis 0 with size 3


time = np.linspace(20, 145, 5)      # time scale
print(time)
# [ 20.    51.25  82.5  113.75 145.  ]

data = np.sin(np.arange(20)).reshape((5, 4))
print(data)
# [[ 0.          0.84147098  0.90929743  0.14112001]
#  [-0.7568025  -0.95892427 -0.2794155   0.6569866 ]
#  [ 0.98935825  0.41211849 -0.54402111 -0.99999021]
#  [-0.53657292  0.42016704  0.99060736  0.65028784]
#  [-0.28790332 -0.96139749 -0.75098725  0.14987721]]

# index of the maxima for each series
ind = data.argmax(axis=0)
print(ind)
# [2 0 3 1]
# col[0] = 0.98935825   = 2
# col[1] = 0.84147098   = 0
# col[2] = 0.99060736   = 3
# col[3] = 0.6569866    = 1

time_max = time[ind]
print(time_max)
# [ 82.5   20.   113.75  51.25]

data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]...
print(data_max)
# [0.98935825 0.84147098 0.99060736 0.6569866 ]

w = np.all(data_max == data.max(axis=0))
print(w)
# True


a = np.arange(5)
print(a)
# [0 1 2 3 4]
a[[1, 3, 4]] = 0
print(a)
# [0 0 2 0 0]

a = np.arange(5)
print(a)
# [0 1 2 3 4]
a[[0, 0, 2]] = [1, 2, 3]
print(a)
# [2 1 3 3 4]

a = np.arange(5)
print(a)
# [0 1 2 3 4]
a[[0, 0, 2]] += 1
print(a)
# [1 1 3 3 4]