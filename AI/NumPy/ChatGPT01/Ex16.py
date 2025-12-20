# Ex16        Mini Linear Regression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

w = 0.0
lr = 0.1

for _ in range(100):
    y_pred = w * X.flatten()
    grad = np.mean(2 * (y_pred - y) * X.flatten())
    w -= lr * grad


print(w)
# 2.0