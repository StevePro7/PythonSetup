from logging import info

import numpy as np

# How to save and load NumPy objects
a = np.array([1, 2, 3, 4, 5, 6])
#np.savetxt("filename.txt", a)

np.save("filename", a)
b = np.load(file="filename.npy")
print(b)
# [1 2 3 4 5 6]


csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt("filename.csv", csv_arr)
c = np.loadtxt("filename.csv", delimiter=",")
print(c)
# [1. 2. 3. 4. 5. 6. 7. 8.]