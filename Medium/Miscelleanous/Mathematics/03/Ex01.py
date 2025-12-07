import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# SIMPLE 1-D EXAMPLE -------------------------------------------------------
# Generate a noisy 1-D sinusoidal data set
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)           # Feature column (0–5)
y = np.sin(X).ravel()                              # True signal
y[::5] += 0.5 - rng.rand(16)                       # Inject some noise

# Fit a shallow regression tree (depth=3)
tree_simple = DecisionTreeRegressor(max_depth=3, random_state=42)
tree_simple.fit(X, y)

# Make predictions on a dense grid for smooth plotting
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_pred = tree_simple.predict(X_test)

# PLOT 1: data and model predictions
plt.figure()
plt.scatter(X, y, s=25, label="Training samples")   # raw data
plt.plot(X_test, y_pred, linewidth=2, label="Tree prediction")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Depth-3 Decision Tree Regression")
plt.legend()
plt.show()

# PLOT 2: visualize the learned tree structure
plt.figure(figsize=(10, 6))
plot_tree(tree_simple, filled=True, rounded=True,
          feature_names=["X"], max_depth=3)
plt.title("Structure of the depth-3 regression tree")
plt.show()

# EFFECT OF TREE DEPTH -----------------------------------------------------
depths = [2, 5, None]  # None = unlimited depth
models = []
for d in depths:
    reg = DecisionTreeRegressor(max_depth=d, random_state=42)
    reg.fit(X, y)
    models.append(reg)

    y_pred = reg.predict(X_test)
    plt.figure()
    plt.scatter(X, y, s=20)
    plt.plot(X_test, y_pred, linewidth=2)
    plt.xlabel("X")
    plt.ylabel("y")
    title = f"Decision Tree (max_depth={d if d else 'None'})"
    plt.title(title)
    plt.show()
