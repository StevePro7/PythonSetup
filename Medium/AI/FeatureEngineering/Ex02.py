from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from my_data import X_train, y_train

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_
data: dict = {
    "feature": X_train.columns,
    "importance": importances
}
feature_importance_df = pd.DataFrame(data).sort_values("importance", ascending=False)
print(feature_importance_df)

# Visualize
plt.barh(feature_importance_df['feature'], feature_importance_df['importance'])
plt.xlabel('Importance')
plt.title('Feature Importance - Random Forest')
plt.show()
