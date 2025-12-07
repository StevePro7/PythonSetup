from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import plot_tree
import numpy as np

# Load the diabetes dataset
data = load_diabetes()
X = data.data
y = data.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit a Decision Tree to get the cost complexity pruning path
tree = DecisionTreeRegressor(random_state=42)
path = tree.cost_complexity_pruning_path(X_train, y_train)

# Extract effective alphas and corresponding total leaf impurities
ccp_alphas = path.ccp_alphas[:-1]  # Drop the last alpha that would prune the tree to a root
impurities = path.impurities[:-1]

# Train a tree for each alpha and store the train/test scores
trees = []
train_scores = []
test_scores = []

for alpha in ccp_alphas:
    model = DecisionTreeRegressor(random_state=42, ccp_alpha=alpha)
    model.fit(X_train, y_train)
    trees.append(model)
    train_scores.append(model.score(X_train, y_train))
    test_scores.append(model.score(X_test, y_test))

# Create a DataFrame to display alpha values and corresponding scores
results_df = pd.DataFrame({
    'alpha': ccp_alphas,
    'train_r2': train_scores,
    'test_r2': test_scores
})


# Find the alpha with the highest test R² score
best_index = np.argmax(test_scores)
best_alpha = ccp_alphas[best_index]
best_model = trees[best_index]

# Show results
best_train_r2 = train_scores[best_index]
best_test_r2 = test_scores[best_index]

# Plot the best tree
plt.figure(figsize=(20, 10))
plot_tree(best_model, feature_names=data.feature_names, filled=True, rounded=True, fontsize=10)
plt.title(f"Best Pruned Decision Tree (alpha={best_alpha:.5f})", fontsize=16)
plt.show()