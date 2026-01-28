# Ex01
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Ex02
from sklearn.metrics import classification_report

# Ex01
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Init model
model = LogisticRegression(max_iter=200)

# Init K-Fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation
print("Performing 5-Fold Cross-Validation...")
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print(f"\nScores for each fold: {scores}")
print(f"Average Accuracy: {scores.mean():.2f}")
print(f"Standard Deviation: {scores.std():.2f}")


# Scores for each fold: [1.         1.         0.93333333 0.96666667 0.96666667]
# Average Accuracy: 0.97
# Standard Deviation: 0.02


# Ex02
# Split data for the report
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model.fit(X_train, y_train)

# Get predictions
y_pred = model.predict(X_test)

# Print the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Classification Report:
#               precision    recall  f1-score   support
#
#       setosa       1.00      1.00      1.00        19
#   versicolor       1.00      1.00      1.00        13
#    virginica       1.00      1.00      1.00        13
#
#     accuracy                           1.00        45
#    macro avg       1.00      1.00      1.00        45
# weighted avg       1.00      1.00      1.00        45
