import numpy as np

# Shape manipulation
## Changing the shape of an array
rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((3, 4)))
print(a)
# [[5. 9. 1. 9.]
#  [3. 4. 8. 4.]
#  [5. 0. 7. 5.]]
print(a.shape)
# (3, 4)

print(a.ravel())
# [5. 9. 1. 9. 3. 4. 8. 4. 5. 0. 7. 5.]

b = a.reshape((6, 2))
print(b)
# [[5. 9.]
#  [1. 9.]
#  [3. 4.]
#  [8. 4.]
#  [5. 0.]
#  [7. 5.]]
print(a.T.shape)
# (4, 3)

print(a.shape)
# (3, 4)


## Stacking together different arrays
a = np.floor(10 * rg.random((2, 2)))
print(a)
# [[3. 7.]
#  [3. 4.]]

b = np.floor(10 * rg.random((2, 2)))
print(b)
# [[1. 4.]
#  [2. 2.]]

print(np.vstack((a, b)))
# [[3. 7.]
#  [3. 4.]
#  [1. 4.]
#  [2. 2.]]

print(np.hstack((a, b)))
# [[3. 7. 1. 4.]
#  [3. 4. 2. 2.]]

from numpy import newaxis
x = np.column_stack((a, b))  # with 2D arrays
print(x)
# [[3. 7. 1. 4.]
#  [3. 4. 2. 2.]]

a = np.array([4., 2.])
b = np.array([3., 8.])
y = np.column_stack((a, b))  # returns a 2D array
print(y)
# [[4. 3.]
#  [2. 8.]]

z = np.hstack((a, b))       # the result is different
print(z)
# [4. 2. 3. 8.]

w = a[:, newaxis]           # view `a` as a 2D column vector
print(w)
# [[4.]
#  [2.]]

u = np.column_stack((a[:, newaxis], b[:, newaxis]))
print(u)
# [[4. 3.]
#  [2. 8.]]

v = np.hstack((a[:, newaxis], b[:, newaxis]))   # the result is the same
# [[4. 3.]
#  [2. 8.]]


## Splitting one array into several smaller ones
a = np.floor(10 * rg.random((2, 12)))
print(a)
# [[7. 2. 4. 9. 9. 7. 5. 2. 1. 9. 5. 1.]
#  [6. 7. 6. 9. 0. 5. 4. 0. 6. 8. 5. 2.]]

b = np.hsplit(a, 3)     # split 'a' into 3
print(b)
# [array([[7., 2., 4., 9.],
#        [6., 7., 6., 9.]]),
#  array([[9., 7., 5., 2.],
#        [0., 5., 4., 0.]]),
#  array([[1., 9., 5., 1.],
#        [6., 8., 5., 2.]])]

c = np.hsplit(a, (3, 4))
print(c)
# [array([[7., 2., 4.],
#        [6., 7., 6.]]),
#  array([[9.],
#        [9.]]),
#  array([[9., 7., 5., 2., 1., 9., 5., 1.],
#        [0., 5., 4., 0., 6., 8., 5., 2.]])]