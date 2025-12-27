import numpy as np

# Indexing, slicing and iterating
a = np.arange(10) ** 3
print(a)
# [  0   1   8  27  64 125 216 343 512 729]

print(a[2])
# 8

print(a[2:5])
# [8 27 64]

a[:6:2] = 1000
# start to =< 6 step 2
# index 0, 2, 4
print(a)
# [1000 1 1000 27 1000 125 216 343 512 729]

print(a[::-1])          # reversed a
# [ 729  512  343  216  125 1000   27 1000    1 1000]

# for i in a:
#     print(round(i ** ( 1/3.)))

bob = [round(i ** (1/3.)) for i in a]
print(bob)
# [10, 1, 10, 3, 10, 5, 6, 7, 8, 9]


def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]
print(hex(b.__array_interface__['data'][0]))
# 0x270601fe750

c = b[2, 3]
print(c)
# 23
print(hex(c.__array_interface__['data'][0]))
# 0x2707e9fc500

print(b[0:5, 1])    # each row in the second column of b
# [ 1 11 21 31 41]

print(b[:, 1])      # equivalent to the previous example)
# [ 1 11 21 31 41]

print(b[1:3, :])    # each column in the second and third row of b
# [[10 11 12 13]
#  [20 21 22 23]]

print(b[-1])        # the last row. Equivalent to b[-1, :]
# [40 41 42 43]


# a 3D array (two stacked 2D arrays)
c = np.array([[[  0,   1,   2],
               [ 10,  11,  13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c)
# [[[  0   1   2]
#   [ 10  11  13]]
#
#  [[100 101 102]
#   [110 112 113]]]
print(c.shape)
# (2, 2, 3)

print(c[1, ...])    # same as c[1, :, :] or c[1]
# [[100 101 102]
#  [110 112 113]]

print(c[..., 2])    # same as c[:, :, 2]
# [[  2  13]
#  [102 113]]


for row in b:
    print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]

x = b.flatten()
print(x)
# [ 0  1  2  3 10 11 12 13 20 21 22 23 30 31 32 33 40 41 42 43]

for element in b.flat:
    print(element)
#
# 0
# 1
# 2
# 3
# 10
# 11
# 12
# 13
# 20
# 21
# 22
# 23
# 30
# 31
# 32
# 33
# 40
# 41
# 42
# 43