# 1. NUMPY
import numpy as np

# Advanced slicing + indexing
a=np.arange(25).reshape(5, 5)
#print(a)

sub = a[1:4, 1:4]
#print(sub)
#print(a[[0, 1, 2], [1, 2, 3]])
#[ 1  7 13]

# Broadcasting
matrix = np.ones((3, 3))
#print(matrix)

matrix += np.array([1, 2, 3])
#print(matrix)

# Random number generation
np.random.seed(42)
#print(np.random.rand(3, 2))
#print(np.random.randint(10, 100, size=(2, 4)))
#print(np.random.normal(loc=0, scale=1, size=5))
#[ 0.49671415 -0.1382643   0.64768854  1.52302986 -0.23415337]

# Vectorization vs. Loops (performance boost)
arr = np.arange(1_000_000)
#loop = slow
one = [ x**2 for x in arr]
#print(one)

# vectorization = fast
two = arr ** 2
# print(two)

# Masking + filtering
arr = np.arange(20)
filtered = arr[arr > 10]
#print(filtered)
#[11 12 13 14 15 16 17 18 19]

# Useful functions at intermediate level
a = np.array([[1, 2], [3, 4], [5, 6]])
#print(a)
#print(a.flatten())
# [1 2 3 4 5 6]

#print(np.repeat([1, 2, 3], 2))
#[1 1 2 2 3 3]

#print(np.tile([1, 2, 3], 2))
#[1 2 3 1 2 3]
