import numpy as np

# Array creation
a = np.array([2, 3, 4])
print(a)
print(a.dtype)
print(hex(a.__array_interface__['data'][0]))

b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)
print(hex(b.__array_interface__['data'][0]))

bb = np.array([(1.5, 2, 3), (4, 5, 6)])
print(bb)
#[[1.5 2.  3. ]
# [4.  5.  6. ]]

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
#[[1.+0.j 2.+0.j]
# [3.+0.j 4.+0.j]]

print(np.zeros((3, 4)))
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]

print(np.ones((2, 3, 4), dtype=np.int16))
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
#
#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]

print(np.empty((2, 3)))
# [[1.39069238e-309 1.39069238e-309 1.39069238e-309]
#  [1.39069238e-309 1.39069238e-309 1.39069238e-309]]

print(np.arange(10, 30, 5))
# [10 15 20 25]

print(np.arange(0, 2, 0.3))
# [0.  0.3 0.6 0.9 1.2 1.5 1.8]

print(np.linspace(0, 2, 9))
# [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]

from numpy import pi
x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)
#print(f)