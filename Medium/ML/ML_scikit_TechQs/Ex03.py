import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction import FeatureHasher
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Synthetic dataset
np.random.seed(42)
n_samples = 5000
n_categories = 1000
X = pd.DataFrame({
    'cat_feature': np.random.randint(0, n_categories, size=n_samples),
    'num_feature': np.random.randn(n_samples)
})
y = (X['num_feature'] + np.random.randn(n_samples)*0.1 > 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Target Encoding ---
# Compute mean target per category on training data only
target_means = X_train.groupby('cat_feature')['num_feature'].mean()
X_train_te = X_train.copy()
X_test_te = X_test.copy()
X_train_te['cat_encoded'] = X_train_te['cat_feature'].map(target_means)
X_test_te['cat_encoded'] = X_test_te['cat_feature'].map(target_means).fillna(target_means.mean())
rf_te = RandomForestClassifier(n_estimators=100, random_state=42)
rf_te.fit(X_train_te[['cat_encoded', 'num_feature']], y_train)
print("Target Encoding Accuracy:", accuracy_score(y_test, rf_te.predict(X_test_te[['cat_encoded','num_feature']])))

# --- Feature Hashing ---
hasher = FeatureHasher(n_features=32, input_type='string')
X_train_hashed = hasher.transform(X_train['cat_feature'].astype(str))
X_test_hashed = hasher.transform(X_test['cat_feature'].astype(str))

# Combine with numeric feature
import scipy.sparse as sp
X_train_combined = sp.hstack([X_train_hashed, X_train[['num_feature']]])
X_test_combined = sp.hstack([X_test_hashed, X_test[['num_feature']]])
rf_hash = RandomForestClassifier(n_estimators=100, random_state=42)
rf_hash.fit(X_train_combined, y_train)
print("Feature Hasher Accuracy:", accuracy_score(y_test, rf_hash.predict(X_test_combined)))

# ValueError: Samples can not be a single string. The input must be an iterable over iterables of strings.