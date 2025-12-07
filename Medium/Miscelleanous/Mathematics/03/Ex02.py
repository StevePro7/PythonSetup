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

# Evaluate performance
# Compute MSE and then take the square root to get RMSE
mse = mean_squared_error(y_te, tree_diab.predict(X_te))
rmse = np.sqrt(mse)
r2_score = tree_diab.score(X_te, y_te)
print(f"Diabetes regression RMSE (depth=8): {rmse:.3f}")
print(f"Diabetes r2_score (depth=8): {r2_score:.3f}")
# PLOT 4: Feature importance bar chart
plt.figure(figsize=(8, 5))
order = np.argsort(tree_diab.feature_importances_)[::-1]
plt.bar(range(len(order)), tree_diab.feature_importances_[order])
plt.xticks(range(len(order)), np.array(data.feature_names)[order],
           rotation=45, ha="right")
plt.ylabel("Importance")
plt.title("Feature importances learned by the tree")
plt.tight_layout()
plt.show()
