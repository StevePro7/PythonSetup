# Ex04        Indexing & Slicing
import numpy as np

# 1D
x = np.array([10, 20, 30, 40])
print(x)
#print(type(x))      # numpy.ndarray
#print(x.shape)      # (4,)

a = x[0]
print(a)            # 10

b = x[-1]
print(b)            # 40

start: int = 1
stop: int = 3
c = x[start : stop]
print(c)            # [20 30]


# 2D
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
#[[1 2 3]
# [4 5 6]]

x = m[0, 1]
print(x)            # 2 = row:0 && col:1

y = m[:, 1]         # col:1 = [2 5]
print(y)

z = m[1, :]         # row:1 = [4 5 6]
print(z)