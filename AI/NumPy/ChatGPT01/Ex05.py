# Ex05        Boolean Masking (Critical for ML)
import numpy as np

x = np.array([1, 2, 3, 4])
y = x[x > 2]
print(y)        # [3 4]