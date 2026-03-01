import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, make_scorer


# Synthetic dataset
X, y = make_classification(n_samples=5000, n_features=20, weights=[0.7, 0.3], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Custom scorer: Precision at 90% Recall
def precision_at_recall_90(y_true, y_scores):
    thresholds = np.linspace(0, 1, 1000)
    for t in thresholds:
        y_pred = (y_scores >= t).astype(int)
        if recall_score(y_true, y_pred) >= 0.9:
            return precision_score(y_true, y_pred)

    return 0.0

# Wrap as Scikit-learn scorer (needs_threshold=True for probabilities)
#scorer = make_scorer(precision_at_recall_90, needs_threshold=True)
scorer = make_scorer(precision_at_recall_90)

# Train model and evaluate
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_scores = model.predict_proba(X_test)[:,1]
precision = precision_at_recall_90(y_test, y_scores)
print(f"Precision at 90% Recall: {precision:.4f}")

# Optional: GridSearchCV using custom scorer
param_grid = {'max_depth': [3, 5, None], 'n_estimators': [50, 100]}
grid = GridSearchCV(model, param_grid, scoring=scorer, cv=3)
grid.fit(X_train, y_train)
print("Best Params:", grid.best_params_)
