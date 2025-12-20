# Ex08        Reductions
import numpy as np

x = np.array([[1, 2],
             [3, 4]])
#print(x)
#[[1 2]
# [3 4]]

a = x.sum()
print(a)        # 10

b = x.mean()
print(b)        # 2.5

c = x.max()
print(c)        # 4

d = x.sum(axis=0)
print(d)        # [4 6]     cols [1+3 2+4]

e = x.sum(axis=1)
print(e)        # [3 7]     rows [1+2 3+4]
