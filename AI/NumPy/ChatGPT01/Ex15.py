# Ex15        Loss Example
import numpy as np

y_true = np.array([1, 0, -1])
y_pred = np.array([0.8, 0.2, 0.6])

loss = np.mean((y_true - y_pred) ** 2)
print(loss)
# 0.8800000000000002