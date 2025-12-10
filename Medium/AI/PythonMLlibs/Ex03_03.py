# 3. SCIKIT-LEARN
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
import numpy as np

# 1. load dataset
X, y = load_iris(return_X_y=True)
target_names = load_iris().target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. define pipeline
pipeline = Pipeline([
    ('features', FeatureUnion([
        ('pca', PCA(n_components=2)),                                # Dimensionality reduction
        ('poly', PolynomialFeatures(degree=2, include_bias=False))   # Feature expansion
    ])),
    ('scaler', StandardScaler()),                                    # Feature scaling
    ('ridge', Ridge())                                               # Ridge regression
])

# 3. define parameter grid for Ridge (alpha values)
param_grid = {'ridge__alpha': [0.1, 1.0, 10.0]}

# 4. GridSearchCV to find best alpha
grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)

# 5. evaluate
print("Best alpha:", grid.best_params_['ridge__alpha'])
print("Best CV score:", grid.best_score_)
# Best alpha: 0.1
# Best CV score: 0.9350956141268736

# 6. final model performance on test set
y_pred = grid.predict(X_test)

# round predictions + clip to valid class labels [0, 1, 2]
y_pred_classes = np.clip(np.round(y_pred).astype(int), 0, 2)

# 7. print classification report
print("\nClassification Report on Test Set:")
print(classification_report(y_test, y_pred_classes, target_names=target_names))