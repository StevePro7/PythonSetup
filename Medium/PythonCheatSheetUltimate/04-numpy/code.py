import numpy as np

# 01.
array = np.array([1, 2, 3, 4, 5])
print(array)


# 02.
zeros = np.zeros((3, 3))  # A 3x3 array of zeros
ones = np.ones((2, 4))  # A 2x4 array of ones
print(zeros)
print(ones)


# 03.
range_array = np.arange(10, 50, 5)  # From 10 to 50, step by 5
print(range_array)
# OUTPUT
# [10 15 20 25 30 35 40 45]


# 04.
linear_spaced = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print(linear_spaced)
# OUTPUT
# [0.   0.25 0.5  0.75 1.  ]


# 05.
reshaped = np.arange(9).reshape(3, 3)  # Reshape a 1D array into a 3x3 2D array
print(reshaped)
# OUTPUT
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]


# 06.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum = a + b         # Element-wise addition
difference = b - a  # Element-wise subtraction
product = a * b     # Element-wise multiplication
print(sum)          # [5 7 9]
print(difference)   # [3 3 3]
print(product)      # [ 4 10 18]


# 07.
result = np.dot(a.reshape(1, 3), b.reshape(3, 1))  # Dot product of a and b
print(result)
# OUTPUT
# [[32]]

# 08.
element = a[2]          # Retrieve the third element of array 'a'
row = reshaped[1, :]    # Retrieve the second row of 'reshaped'
print(row)
# OUTPUT
# [3 4 5]


# 09.
filtered = a[a > 2]  # Elements of 'a' greater than 2
print(filtered)
# OUTPUT
# [3]


10.
mean = np.mean(a)
maximum = np.max(a)
sum = np.sum(a)
print(mean)         # 2.0
print(maximum)      # 3
print(sum)          # 6




