import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')

# Step 6: Model Evaluation and Hyperparameter Tuning

X = data.drop('Outcome', axis=1)
y = data['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# cross-validation: get better estimate of model performance
from sklearn.model_selection import cross_val_score
# scores = cross_val_score(RandomForestClassifier(), X, y, cv=5)
# print(scores.mean())
# 0.7735251676428148


# hyperparameter tuning with Grid Search or Randomized Search
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None]
}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
# {'max_depth': 20, 'n_estimators': 300}


# evaluate on Test set
best_model = grid_search.best_estimator_
y_pred_test = best_model.predict(X_test)
print("beg")
print(classification_report(y_test, y_pred_test))
print("end")
