import numpy as np

# How do you know the shape and size of an array?
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example.shape)
# (3, 2, 4)


# Reshape
a = np.arange(6)
b = a.reshape(3, 2)
print(b)
# [[0 1]
#  [2 3]
#  [4 5]]

c = np.reshape(a, shape=(1, 6), order='C')
print(c)
# [[0 1 2 3 4 5]]


# How to convert a 1D array into a 2D array (how to add a new axis to an array)
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
# (6,)

a2 = a[np.newaxis, :]
print(a2.shape)
# (1, 6)

row_vector = a[np.newaxis, :]
print(row_vector.shape)
# (1, 6)

col_vector = a[:, np.newaxis]
print(col_vector.shape)
# (6, 1)


a = np.array([1, 2, 3, 4, 5,6])
print(a.shape)
# (6,)

b = np.expand_dims(a, axis=1)
print(b.shape)
# (6, 1)

