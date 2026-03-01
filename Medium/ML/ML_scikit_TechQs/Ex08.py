from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter space
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5]
}
param_dist = {
    'n_estimators': [50, 100, 200, 300, 400],
    'max_depth': [None, 5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'max_features': ['sqrt', 'log2', None]
}

# GridSearchCV (exhaustive)
grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                           param_grid=param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train, y_train)
print("GridSearch Best Params:", grid_search.best_params_)
#score = accuracy_score(y_test, grid_search.predict(X_test))
print("GridSearch Test Accuracy:", accuracy_score(y_test, grid_search.predict(X_test)))

# RandomizedSearchCV (random sampling)
random_search = RandomizedSearchCV(RandomForestClassifier(random_state=42),
                                   param_distributions=param_dist,
                                   n_iter=10, cv=3, scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)
print("RandomizedSearch Best Params:", random_search.best_params_)
#score = accuracy_score(y_test, random_search.predict(X_test))
print("RandomizedSearch Test Accuracy:", accuracy_score(y_test, random_search.predict(X_test)))