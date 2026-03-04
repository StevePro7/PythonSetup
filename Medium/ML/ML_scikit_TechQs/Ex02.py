import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

# Load dataset
X, y = load_breast_cancer(return_X_y=True)
feature_names = load_breast_cancer().feature_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a black-box model
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

# Default feature importances (may be biased)
print("Default Feature Importances:")
for name, score in zip(feature_names, rf.feature_importances_):
    print(f"{name}: {score:.4f}")

# Permutation importance (more reliable)
perm_importance = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=42)
sorted_idx = perm_importance.importances_mean.argsort()[::-1]
print("\nPermutation Importances:")
for idx in sorted_idx[:10]:  # top 10
    print(f"{feature_names[idx]}: {perm_importance.importances_mean[idx]:.4f} ± {perm_importance.importances_std[idx]:.4f}")


# Default Feature Importances:
# mean radius: 0.0504
# mean texture: 0.0147
# mean perimeter: 0.0383
# mean area: 0.0425
# mean smoothness: 0.0085
# mean compactness: 0.0149
# mean concavity: 0.0558
# mean concave points: 0.1198
# mean symmetry: 0.0036
# mean fractal dimension: 0.0045
# radius error: 0.0165
# texture error: 0.0042
# perimeter error: 0.0079
# area error: 0.0235
# smoothness error: 0.0043
# compactness error: 0.0050
# concavity error: 0.0099
# concave points error: 0.0039
# symmetry error: 0.0047
# fractal dimension error: 0.0062
# worst radius: 0.0693
# worst texture: 0.0210
# worst perimeter: 0.1271
# worst area: 0.1285
# worst smoothness: 0.0130
# worst compactness: 0.0177
# worst concavity: 0.0407
# worst concave points: 0.1283
# worst symmetry: 0.0098
# worst fractal dimension: 0.0052
