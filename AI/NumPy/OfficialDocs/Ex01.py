import numpy as np

# An example
a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.dtype)
print(hex(a.__array_interface__['data'][0]))