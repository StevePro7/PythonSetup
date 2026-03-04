from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Synthetic dataset
X, y = make_classification(n_samples=5000, n_features=20, n_informative=15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# GradientBoostingClassifier with early stopping
gbm = GradientBoostingClassifier(
    n_estimators=500,
    learning_rate=0.1,
    validation_fraction=0.1,  # 10% of training set for early stopping
    n_iter_no_change=10,      # stop if no improvement in 10 rounds
    tol=1e-4,
    random_state=42
)

# Train
gbm.fit(X_train, y_train)

# Evaluate
y_pred = gbm.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Number of trees used: {gbm.n_estimators_}")

# Test Accuracy: 0.9520
# Number of trees used: 500