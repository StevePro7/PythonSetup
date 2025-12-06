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

p=np.array([[1, 2, 3], [5, 6, 7]])
q=np.array([[11, 12, 13], [15, 16, 17]])
added_arr=np.concatenate((p, q), axis=0)
#print(added_arr)

res=np.add(p, q)
#print(res)

res1=np.multiply(p, q)
#print(res1)

res2=np.subtract(p, q)
#print(res2)

res3=np.divide(p, q)
#print(res3)

rand=np.arange(10)

print(rand[3:])