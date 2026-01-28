# 1. NUMPY
import numpy as np

# memory views + stride tricks
a = np.arange(16).reshape(4, 4)
#print(a)

# create sliding window view 2x2
from numpy.lib.stride_tricks import sliding_window_view
windows = sliding_window_view(a, (2,2))
#print("Sliding windows shape:", windows.shape)
#print("Windows:\n", windows[0,0])

# broadcasting tricks for efficient computation
b = np.array([1,2,3,4])
c = np.arange(4).reshape(4,1)
#print("Broadcasted sum:\n", b + c)

#print(np.dot(a, a))
