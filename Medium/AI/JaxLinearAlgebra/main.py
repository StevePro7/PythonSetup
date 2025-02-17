import jax.numpy as jnp
import jax
import matplotlib.pyplot as plt

# Generate synthetic data
key = jax.random.PRNGKey(0)
x = jax.random.uniform(key, (100,), minval=0, maxval=10)
true_w, true_b = 2.5, 1.0  # True slope and intercept
y = true_w * x + true_b + jax.random.normal(key, (100,))  # Adding some noise

# Initialize parameters
w = jnp.array(0.0)
b = jnp.array(0.0)

# Define the linear model
def model(w, b, x):
    return w * x + b

# Define the loss function (Mean Squared Error)
def loss_fn(w, b, x, y):
    y_pred = model(w, b, x)
    return jnp.mean((y_pred - y) ** 2)

# Compute gradients
grad_fn = jax.grad(loss_fn, argnums=(0, 1))  # Compute gradients for w and b

# Gradient Descent Update
def update(w, b, x, y, lr=0.01):
    dw, db = grad_fn(w, b, x, y)
    w = w - lr * dw
    b = b - lr * db
    return w, b

# Training loop
epochs = 100
learning_rate = 0.05
for epoch in range(epochs):
    w, b = update(w, b, x, y, learning_rate)

# Plot results
plt.scatter(x, y, label="Data")
plt.plot(x, model(w, b, x), color='red', label="Fitted Line")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression with JAX")
plt.show()

print(f"Learned parameters: w = {w:.3f}, b = {b:.3f}")
print(f"True parameters: w = {true_w}, b = {true_b}")
