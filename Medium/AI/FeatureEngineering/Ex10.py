from sklearn.ensemble import RandomForestClassifier
from my_data import X_train, X_test, y_train, y_test
import pandas as pd

# Train baseline model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Get feature importances
data: dict = {
    "feature": X_train.columns,
    "importance": model.feature_importances_
}
importances = pd.DataFrame(data).sort_values("importance", ascending=False)
print(importances)

# Remove low-importance features (< 1% importance)
important_features = importances[importances["importance"] > 0.01]["feature"].tolist()
X_train = X_train[important_features]
X_test = X_test[important_features]
