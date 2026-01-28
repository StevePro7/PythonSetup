# 4. SCIKIT-LEARN
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

iris = datasets.load_iris()
X = iris.data
y = iris.target

# 1. load dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. feature scaling (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. cross validation = evaluate model stability
model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print(f"Cross-validation scores: {scores}")
print(f"Mean CV accuracy: {scores.mean():.4f}")
# Cross-validation scores: [0.95833333 1.         0.875      1.         0.95833333]
# Mean CV accuracy: 0.9583

# 4. pipeline to chain scaling + model
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
#print("Classification Report:\n", classification_report(y_test, y_pred))

# 5. model comparison
models = [
    ('Logistic Regression', LogisticRegression(max_iter=200)),
    ('Random Forest', RandomForestClassifier(random_state=42))
]

for name, model in models:
    pipe = Pipeline([('scaler', StandardScaler()), ('model', model)])
    pipe.fit(X_train, y_train)
    score = pipe.score(X_test, y_test)
    print(f"{name} Accuracy: {score:.4f}")
# Logistic Regression Accuracy: 1.0000
# Random Forest Accuracy: 1.0000

