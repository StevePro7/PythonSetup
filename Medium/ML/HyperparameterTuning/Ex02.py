# Import necessary libraries
import pandas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint, uniform
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Define the model
rf_clf = RandomForestClassifier(random_state=42)

# 2. Define the hyperparameter distributions/values
# 'n_estimators': number of trees in the forest
# 'max_depth': maximum depth of the tree
# 'min_samples_split': minimum number of samples required to split an internal node
# 'min_samples_leaf': minimum number of samples required to be at a leaf node
# 'bootstrap': whether bootstrap samples are used when building trees
param_dist = {
    'n_estimators': randint(50, 200),  # Random integer between 50 and 200
    'max_depth': randint(3, 15),       # Random integer between 3 and 15
    'min_samples_split': randint(2, 20), # Random integer between 2 and 20
    'min_samples_leaf': randint(1, 10),  # Random integer between 1 and 10
    'bootstrap': [True, False],
    'criterion': ['gini', 'entropy']
}

print("Hyperparameter distributions/values defined:")
print(param_dist)
# {'n_estimators': <scipy.stats._distn_infrastructure.rv_discrete_frozen object at 0x00000233648A4990>, 'max_depth': <scipy.stats._distn_infrastructure.rv_discrete_frozen object at 0x00000233677ECAD0>, 'min_samples_split': <scipy.stats._distn_infrastructure.rv_discrete_frozen object at 0x00000233677ED1D0>, 'min_samples_leaf': <scipy.stats._distn_infrastructure.rv_discrete_frozen object at 0x00000233677ED8D0>, 'bootstrap': [True, False], 'criterion': ['gini', 'entropy']}

# 3. Initialize RandomizedSearchCV
# n_iter: number of parameter settings that are sampled (the budget)
random_search = RandomizedSearchCV(estimator=rf_clf,
                                   param_distributions=param_dist,
                                   n_iter=50,       # Try 50 different combinations
                                   cv=5,
                                   scoring='accuracy',
                                   n_jobs=-1,
                                   random_state=42,
                                   verbose=1)

print("\nStarting RandomizedSearchCV...")

# 4. Fit RandomizedSearchCV to the training data
random_search.fit(X_train, y_train)
# Fitting 5 folds for each of 50 candidates, totalling 250 fits
print("RandomizedSearchCV complete!")

# 5. Get the best parameters and best score
print(f"\nBest parameters found: {random_search.best_params_}")
print(f"Best cross-validation accuracy: {random_search.best_score_:.2f}")
# Best parameters found: {'bootstrap': True, 'criterion': 'gini', 'max_depth': 13, 'min_samples_leaf': 8, 'min_samples_split': 5, 'n_estimators': 153}
# Best cross-validation accuracy: 0.95

# 6. Evaluate the best model on the test set
best_rf_model = random_search.best_estimator_
y_pred_rf = best_rf_model.predict(X_test)
print(f"\nTest set accuracy with best model: {accuracy_score(y_test, y_pred_rf):.2f}")
# Test set accuracy with best model: 1.00

print("\nClassification Report on Test Set:")
print(classification_report(y_test, y_pred_rf, target_names=iris.target_names))
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