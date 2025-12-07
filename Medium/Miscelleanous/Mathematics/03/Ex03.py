import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# REAL-WORLD MULTIVARIATE EXAMPLE (Diabetes dataset) -----------------------
data = load_diabetes()
X_diab, y_diab = data.data, data.target

# Train/test split
X_tr, X_te, y_tr, y_te = train_test_split(X_diab, y_diab,
                                          test_size=0.2,
                                          random_state=42)

# Fit a deeper tree
tree_diab = DecisionTreeRegressor(max_depth=8, min_samples_leaf=30,
                                  random_state=42)
tree_diab.fit(X_tr, y_tr)

# Calculate cumulative feature importances
sorted_indices = np.argsort(tree_diab.feature_importances_)[::-1]
sorted_importances = tree_diab.feature_importances_[sorted_indices]
cumulative_importances = np.cumsum(sorted_importances)

# Create cumulative importance plot
plt.figure(figsize=(8, 5))
plt.plot(range(len(cumulative_importances)), cumulative_importances, marker='o', linestyle='-')
plt.xticks(range(len(sorted_indices)), np.array(data.feature_names)[sorted_indices], rotation=45, ha="right")
plt.ylabel("Cumulative Importance")
plt.xlabel("Features (ranked by importance)")
plt.title("Cumulative feature importances learned by the tree")
plt.grid(axis='y')
plt.tight_layout()
plt.show()