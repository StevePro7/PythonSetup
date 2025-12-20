# Ex13        Data Normalization
import numpy as np

X = np.array([10, 20, 30])

Y = (X - X.mean() / X.std())
print(Y)
# [ 7.55051026 17.55051026 27.55051026]