import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Let's center roughly around median-ish values
X = np.array([
    [65-67, 133-140],   # roughly centered
    [72-67, 160-140],
    [70-67, 152-140],
    [60-67, 120-140]
])   # shape: (4, 2)

y = np.array([[0], [1], [1], [0]])   # (4, 1)


np.random.seed(42)

# Layer 1 (input → hidden)
W1 = np.random.randn(2, 4) * 0.3    # smaller init → stabler start
b1 = np.zeros((1, 4))

# Layer 2 (hidden → output)
W2 = np.random.randn(4, 1) * 0.3
b2 = np.zeros((1, 1))

# Forward pass (one time - no training yet)
z1 = X @ W1 + b1
a1 = sigmoid(z1)           # (4,4)
z2 = a1 @ W2 + b2
y_hat = sigmoid(z2)        # (4,1)

print("Random network predictions (terrible):")
print(y_hat.flatten().round(3))
# Random network predictions (terrible):
# [0.503 0.426 0.428 0.514]