import numpy as np

# Copies and views

## No copy at all
a = np.array([[0, 1, 2, 3],
             [4, 5, 6, 7],
             [8, 9, 10, 11]])
print(hex(a.__array_interface__['data'][0]))
# 0x265c9d1e880

b = a
print(hex(b.__array_interface__['data'][0]))
# 0x265c9d1e880

print(b is a)
# True


def f(x):
    print(id(x))

print(id(a))
# 2472214555376
print(id(b))
# 2472214555376


## View or shallow copy
c = a.view()
print(hex(c.__array_interface__['data'][0]))
# 0x181576055b0

print(c is a)
# False

print(c.base is a)
# True

print(c.flags.owndata)
# False

c = c.reshape((2, 6))
print(c)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

print(a.shape)
# (3, 4)

c[0, 4] = 1234
print(a)
# [[   0    1    2    3]
#  [1234    5    6    7]
#  [   8    9   10   11]]

s = a[:, 1:3]
print(s)
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]]

s[:] = 10       # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print(a)
# [[   0   10   10    3]
#  [1234   10   10    7]
#  [   8   10   10   11]]


## Deep copy
d = a.copy()    # a new array object with new data is created
print(hex(d.__array_interface__['data'][0]))
# 0x20a49720c80

print(d is a)
# False

print(d.base is a)  # d doesn't share anything with a
# False
d[0, 0] = 9999
print(a)
# [[   0   10   10    3]
#  [1234   10   10    7]
#  [   8   10   10   11]]
