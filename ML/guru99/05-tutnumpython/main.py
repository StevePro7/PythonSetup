# https://www.guru99.com/numpy-tutorial.html
# 01-Jan-2019

import tensorflow as tf
import numpy as np

print(np.__version__)
# print('hi')

# Create array list
myPythonList = [1, 9, 0, 3]
print(myPythonList)

# Directly in numpy
numpy_array_from_list = np.array(myPythonList)
print(numpy_array_from_list)

np.array([1, 9, 8, 3])

# Shape
a = np.array([1, 2, 3])
print(a.shape)

# = Type
print(a.dtype)

# 2D array
c = np.array([(1, 2, 3),
              (4, 5, 6)])
print("2D array", c)

# 3D array
d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]
])
print("3D array", d)

# Reshape
e = np.array([(1, 2, 3), (4, 5, 6)])
print("Before reshape")
print(e)
e.reshape(3, 2)
print("After reshape", e)

# Flatten
e.flatten()
print("After flatten", e)

# hastack & vstack
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print("Horz append:", np.hstack((f, g)))
print("Vert append:", np.vstack((f, g)))

# Random number
normal_array = np.random.normal(5, 0.5, 10)
print("Random number", normal_array)

# asarray
A = np.matrix(np.ones((4, 4)))
np.asarray(A)
print("Asarray", A)

# Arrange
print("Arrange", np.arange(1, 11))

# Linspace
lin = np.linspace(1.0, 5.0, num=10)
print("Linespace", lin)

# Logspace
log1 = np.logspace(3.0, 4.0, num=4)
print("Logspace", log1)

# Slicing rows
e = np.array([(1, 2, 3), (4, 5, 6)])
print("Slice row", e[0])

# Slicing cols
print("Slice col", e[:1])

# Slice row + col
print("Slice R+C", e[1, :2])

