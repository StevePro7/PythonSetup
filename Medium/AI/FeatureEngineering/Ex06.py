from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from my_data import X_train, y_train
import matplotlib.pyplot as plt

model = RandomForestClassifier()

# Recursive Feature Elimination with Cross-Validation
rfecv = RFECV(estimator=model, step=1, cv=5)
rfecv.fit(X_train, y_train)

# Get selected features
selected_features = X_train.columns[rfecv.support_].tolist()
print(f"Selected features: {selected_features}")
print(f"Number of features: {rfecv.n_features_}")

# Plot feature ranking
plt.barh(X_train.columns, rfecv.ranking_)
plt.xlabel('Ranking (1 = selected)')
plt.show()
