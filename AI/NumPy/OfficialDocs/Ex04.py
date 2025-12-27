import numpy as np

# Basic operations
a = np.array([20, 30, 40, 50])
print(a)
print(hex(a.__array_interface__['data'][0]))
# [20 30 40 50]
# 0x19ece35f8d0

b = np.arange(4)
print(b)
print(hex(a.__array_interface__['data'][0]))
# [0 1 2 3]
# 0x282f4b57a70

c = a - b
print(c)
print(hex(c.__array_interface__['data'][0]))
# [20 29 38 47]
# 0x22bdfb672d0

d = b ** 2
print(d)
print(hex(d.__array_interface__['data'][0]))
# [0 1 4 9]
# 0x2ebe2014120

e = np.sin(a) * 10
print(e)
print(hex(e.__array_interface__['data'][0]))
# [ 9.12945251 -9.88031624  7.4511316  -2.62374854]
# 0x20b55e016a0

f = a < 35
print(f)
print(hex(f.__array_interface__['data'][0]))
# [ True  True False False]
# 0x297f92d4900


A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A * B)        # elementwise product
# [[2 0]
#  [0 4]]

print(A @ B)        # matrix product
# [[5 4]
#  [3 4]]

print(A.dot(B))     # another matrix product
# [[5 4]
#  [3 4]]


rg = np.random.default_rng(1)
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
print(a)
# [[1 1 1]
#  [1 1 1]]

a *= 3
print(a)
# [[3 3 3]
#  [3 3 3]]

print(b)
# [[0.51182162 0.9504637  0.14415961]
#  [0.94864945 0.31183145 0.42332645]]
b += a
print(b)
# [[3.51182162 3.9504637  3.14415961]
#  [3.94864945 3.31183145 3.42332645]]

# print(a + b)
# No error here but website gives Traceback?


a = np.ones(3, dtype=np.int32)
print(a)

from numpy import pi
b = np.linspace(0, pi, 3)
print(b)
# [0.         1.57079633 3.14159265]
print(b.dtype.name)
# float64

c = a + b
print(c)
# [1.         2.57079633 4.14159265]
print(c.dtype.name)
# float64

d = np.exp(c * 1j)
print(d)
# [ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]
print(d.dtype.name)
# complex128


a = rg.random((2, 3))
print(a)
# [[0.82770259 0.40919914 0.54959369]
#  [0.02755911 0.75351311 0.53814331]]

print(a.sum())
# 3.1057109529998157

print(a.min())
# 0.027559113243068367

print(a.max())
# 0.8277025938204418


b = np.arange(12).reshape((3, 4))
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(b.sum(axis=0))
# [12 15 18 21]

print(b.min(axis=1))
# [0 4 8]

print(b.cumsum(axis=1))
# [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]
