# Import necessary libraries
import pandas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Define the model
dtree = DecisionTreeClassifier(random_state=42)

# 2. Define the hyperparameter grid
# We want to tune "max_depth" and "min_samples_split"
param_grid = {
    "max_depth": [3, 5, 7, None],       # None means no limit
    "min_samples_split": [2, 5, 10],
    "criterion": ["gini", "entropy"]
}

print("Hyperparameter grid defined:")
print(param_grid)
# {'max_depth': [3, 5, 7, None], 'min_samples_split': [2, 5, 10], 'criterion': ['gini', 'entropy']}

# 3. Initialize GridSearchCV
# estimator: the model we want to tune
# param_grid: the dictionary of hyperparameters to test
# cv: number of folds for cross-validation
# verbose: controls the verbosity: higher value means more messages
grid_search = GridSearchCV(estimator=dtree,
                           param_grid=param_grid,
                           cv=5,                    # 5-fold cross-validation
                           scoring="accuracy",
                           n_jobs=-1,               # use all available cores
                           verbose=1)
print("\nStarting GridSearchCV...")

# 4. Fit GridSearchCV to the training data
grid_search.fit(X_train, y_train)
# Fitting 5 folds for each of 24 candidates, totalling 120 fits
print("GridSearchCV complete!")

# 5. Get the best parameters and best score
print(f"\nBest parameters found: {grid_search.best_params_}")
print(f"Best cross-validation accuracy: {grid_search.best_score_:.2f}")
# Best parameters found: {'criterion': 'gini', 'max_depth': 5, 'min_samples_split': 10}
# Best cross-validation accuracy: 0.94


# 6. Evaluate the best model on the test set
best_dtree_model = grid_search.best_estimator_
y_pred = best_dtree_model.predict(X_test)
print(f"\nTest set accuracy with best model: {accuracy_score(y_test, y_pred):.2f}")
# Test set accuracy with best model: 1.00

print("\nClassification Report on Test Set:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
# Classification Report on Test Set:
#               precision    recall  f1-score   support
#
#       setosa       1.00      1.00      1.00        19
#   versicolor       1.00      1.00      1.00        13
#    virginica       1.00      1.00      1.00        13
#
#     accuracy                           1.00        45
#    macro avg       1.00      1.00      1.00        45
# weighted avg       1.00      1.00      1.00        45