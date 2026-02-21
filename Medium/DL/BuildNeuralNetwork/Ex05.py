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

#print("Random network predictions (terrible):")
#print(y_hat.flatten().round(3))
# Random network predictions (terrible):
# [0.503 0.426 0.428 0.514]


def bce_loss(y_true, y_pred):
    # tiny epsilon prevent log(0)
    eps = 1e-8
    return -np.mean(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))


# -----------------------
#        BACKPROP
# -----------------------

# Output layer gradients
dz2 = y_hat - y                        # (4,1)   ← magic simplification!
dW2 = (a1.T @ dz2) / len(X)            # (4,1)
db2 = dz2.mean(axis=0, keepdims=True)  # (1,1)

# Hidden layer gradients
da1 = dz2 @ W2.T                       # (4,4)
dz1 = da1 * a1 * (1 - a1)              # sigmoid derivative
dW1 = (X.T @ dz1) / len(X)             # (2,4)
db1 = dz1.mean(axis=0, keepdims=True)  # (1,4)

learning_rate = 0.15
epochs = 4000

for epoch in range(epochs):

    # Forward
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    y_hat = sigmoid(z2)
    loss = bce_loss(y, y_hat)

    # Backward
    dz2 = y_hat - y
    dW2 = a1.T @ dz2 / len(X)
    db2 = dz2.mean(axis=0, keepdims=True)
    dz1 = (dz2 @ W2.T) * a1 * (1 - a1)
    dW1 = X.T @ dz1 / len(X)
    db1 = dz1.mean(axis=0, keepdims=True)

    # Update
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    # if epoch % 400 == 0:
    #     print(f"epoch {epoch:4d}   loss = {loss:.4f}")


person = np.array([[68-67, 145-140]])   # ~68 inches, 145 lbs
z1 = person @ W1 + b1
a1 = sigmoid(z1)
z2 = a1 @ W2 + b2
prob = sigmoid(z2)[0,0]

print(f"Probability male: {prob:.3f}")
print("→ male" if prob > 0.5 else "→ female")
# Probability male: 0.998
# → male
