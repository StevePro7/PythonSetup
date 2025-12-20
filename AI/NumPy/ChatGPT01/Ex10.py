# Ex10        Linear Algebra
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
#print(A)
#[[1 2]
# [3 4]]

B = np.array([[5, 6],
              [7, 8]])
#print(B)
#[[5 6]
# [7 8]]

# Matrix multiply
c = A @ B
#print(c)
#[[19 22]
# [43 50]]

d = np.dot(A, B)
#print(d)
#[[19 22]
# [43 50]]

e = np.matmul(A, B)
#print(e)
#[[19 22]
# [43 50]]

f = A.T
#print(f)
#[[1 3]
# [2 4]]

g = np.linalg.inv(A)
print(g)
#[[-2.   1. ]
#    [ 1.5 -0.5]]