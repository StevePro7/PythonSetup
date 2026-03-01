from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time


# Generate synthetic dataset
X, y = make_classification(
    n_samples=100000, n_features=50, n_informative=20, n_redundant=10,
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Default RandomForest (slow)
default_rf = RandomForestClassifier(random_state=42)
start = time.time()
default_rf.fit(X_train, y_train)
end = time.time()
print(f"Default RF training time: {end - start:.2f}s")

# Optimized RandomForest
optimized_rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_leaf=5,
    max_features='sqrt',  # limits features per split
    n_jobs=-1,            # use all CPUs
    random_state=42
)

start = time.time()
optimized_rf.fit(X_train, y_train)
end = time.time()
print(f"Optimized RF training time: {end - start:.2f}s")

# Evaluate
y_pred = optimized_rf.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
