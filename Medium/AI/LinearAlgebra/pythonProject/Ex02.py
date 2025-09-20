import numpy as np

# Matrix of house features
X = np.array([  [1200, 3, 10],
                [1500, 4, 5],
                [1000, 2, 10]])

# Weights (co-efficients for size, rooms, age)
W = np.array([200, 10000, -500])

# Predictions
Y = np.dot(X, W)
print("Predicted prices: " , Y)
