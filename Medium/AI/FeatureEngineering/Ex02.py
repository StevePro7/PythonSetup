from sklearn.inspection import permutation_importance
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from my_data import X_train, y_train, X_test, y_test

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

result = permutation_importance(
    model, X_test, y_test,
    n_repeats=10,
    random_state=42
)
# Get feature importances
importances = model.feature_importances_
data: dict = {
    "feature": X_test.columns,
    "importance": result.importances_mean,
    "std": result.importances_std
}
print(importances)

# [0.0373106  0.04856612 0.05092833 0.04743393 0.03357098 0.02003289
#  0.0183006  0.06202435 0.03033342 0.03942747 0.01714911 0.10744472
#  0.037674   0.01503323 0.14998346 0.06570327 0.05456654 0.09046945
#  0.05881018 0.01523735]