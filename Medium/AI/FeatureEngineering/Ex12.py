import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from my_data import X_train, X_test, y_train, y_test

# Load data
df = pd.read_csv("data.csv")

# Init clean
df = df.dropna()

# Separate features and target
X = df.drop("price", axis=1)
y = df["price"]

# Quick correlation check
correlation = X.corrwith(y).sort_values(ascending=False)
print(f"Top 10 correlated features:\n{correlation.head(10)}")

# Remove constant columns
X = X.loc[:, X.std() > 0]

# Train baseline
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

baseline_r2 = model.score(X_test, y_test)
print(f"\nBaseline R² Score: {baseline_r2:.4f}")

# Tree-based importance
data: dict = {
    "feature": X_train.columns,
    "importance": model.feature_importances_
}
tree_importance = pd.DataFrame(data).sort_values("importance", ascending=False)
print(f"\nTop 10 Important Features:\n{tree_importance.head(10)}")

# Permutation importance (more reliable)
perm_importance = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)



