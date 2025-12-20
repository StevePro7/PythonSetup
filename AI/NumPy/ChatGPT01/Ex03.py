import numpy as np

# Common constructors
shape: tuple = (2, 3)
a = np.zeros(shape)
#print(a)
#[[0. 0. 0.]
# [0. 0. 0.]]

b = np.ones(shape)
#print(b)
#[[1. 1. 1.]
# [1. 1. 1.]]

c = np.eye(3)
#print(c)
#[[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]

start: int = 0
stop: int = 10
step: int = 2
d = np.arange(start, stop, step)
#print(d)
#[0 2 4 6 8]

start: int = 0
stop: int = 1
num: int = 5
e = np.linspace(start, stop, num)
#print(e)
# [0.   0.25 0.5  0.75 1.  ]

f = np.random.rand(2, 3)
print(f)
#[[0.31696435 0.66790789 0.4955684 ]
# [0.15987739 0.0612612  0.11257774]]

g = np.random.randn(2, 3)
print(g)
