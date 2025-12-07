# 1. NUMPY
import numpy as np

a=np.arange(100)
a=a.reshape(10, 10)
#print(a)

flatten=a.flatten(order="F")
#print(flatten)

flatten=a.flatten(order="C")
#print(flatten)

b=np.transpose(a)
#print(b)

# JOINING OF ARRAY
p=np.array([[1, 2, 3], [5, 6, 7]])
q=np.array([[11, 12, 13], [15, 16, 17]])
added_arr=np.concatenate((p, q), axis=0)
#print(added_arr)

# ARITHMETIC OPERATIONS
res=np.add(p, q)
#print(res)

res1=np.multiply(p, q)
#print(res1)

res2=np.subtract(p, q)
#print(res2)

res3=np.divide(p, q)
#print(res3)

# SLICING
rand=np.arange(1000)
#print(rand[900:])
#print(rand[:100])

var=slice(90, 100, 1)
#print(rand[var])

# ITERATING OVER ARRAY
trail=np.arange(0, 50, 5)
#for i in np.nditer(trail):
#    print(i)

# RxC = 2x rows X 5 cols
trail=np.arange(0, 50, 5).reshape(2, 5)
#for i in np.nditer(trail, order="F"):
#    print(i)

import matplotlib.pyplot as plt
x=np.arange(0, 3* np.pi, 0.1)
y=np.sin(x)
plt.plot(x, y)
#plt.show()
