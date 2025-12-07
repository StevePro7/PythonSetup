import numpy as np

# Step 1: Input data (imagine it's "study hours")
x = np.array([2])  # 2 hours studied

# Step 2: Weight and bias (parameters the neuron learns)
w = np.array([0.5])  # weight
b = 0.1              # bias

# Step 3: Linear combination (algebra: w*x + b)
z = np.dot(w, x) + b
print("Linear output (z):", z)

# Step 4: Activation function (squish it between 0 and 1)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

a = sigmoid(z)
print("Neuron output (a):", a)
