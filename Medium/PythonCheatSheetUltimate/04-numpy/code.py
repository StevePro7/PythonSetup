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


# 04.
linear_spaced = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print(linear_spaced)


# 05.
reshaped = np.arange(9).reshape(3, 3)  # Reshape a 1D array into a 3x3 2D array
print(reshaped)


# 06.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum = a + b  # Element-wise addition
difference = b - a  # Element-wise subtraction
product = a * b  # Element-wise multiplication
print(sum)
print(difference)
print(product)


# 07.
result = np.dot(a.reshape(1, 3), b.reshape(3, 1))  # Dot product of a and b
print(result)


# 08.
element = a[2]  # Retrieve the third element of array 'a'
row = reshaped[1, :]  # Retrieve the second row of 'reshaped'
print(row)


# 09.
filtered = a[a > 2]  # Elements of 'a' greater than 2
print(filtered)


10.
mean = np.mean(a)
maximum = np.max(a)
sum = np.sum(a)
print(mean)
print(maximum)
print(sum)
