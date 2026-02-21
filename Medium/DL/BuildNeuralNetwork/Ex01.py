import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Example: one input, one weight, one bias
x = 0.8
w = 1.5
b = -0.9
z = w * x + b               # linear part
y = sigmoid(z)
print(f"Output: {y:.4f}")   # value between 0 and 1
# Output: 0.5744