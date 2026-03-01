10 Scikit-learn for Machine Learning Technical Questions Asked in FAANG
01-Mar-2026

https://medium.com/@Rohan_Dutt/10-scikit-learn-for-machine-learning-technical-questions-asked-in-faang-5eeb50d6e75b

uv add numpy
uv add matplotlib
uv add scikit-learn


10. Explain the Bias-Variance Tradeoff Using Scikit-learn Metrics
connect MSE Mean Squared Error to bias and variance

high bias       underfit        high training error
high variance   overfit         large gap btwn training + validation errors

scikit-learn
learning_curve or validation_curve functions


9. How Would You Optimize a Slow RandomForestClassifier?
lists hyperparameters to tweak

optimized hyperparameters significantly reduce training time
accuracy stable or maybe improves due to regularization

Default RF training time: 48.23s
Optimized RF training time: 5.09s
Test Accuracy: 0.9516


8. When Would You Use GridSearchCV Over RandomizedSearchCV?
show awareness of trade-offs btwn exhaustive [GridSearchCV] 
and stochastic search [RandomizedSearchCV]
 
GridSearchCV        small spaces
RandomizedSearchCV  large high-dimensional spaces

GridSearch Best Params: {'max_depth': None, 'min_samples_split': 2, 'n_estimators': 50}
GridSearch Test Accuracy: 1.0
RandomizedSearch Best Params: {'n_estimators': 400, 'min_samples_split': 5, 'max_features': 'sqrt', 'max_depth': None}
RandomizedSearch Test Accuracy: 1.0


7. Debug a Model with 99% Training Accuracy but 60% Test Accuracy
screams overfitting so diagnose the root cause

Debugging
- check for label leakage
- run cross-validation i.e. cross_val_score
- simplify the model i.e. DEC max_depth or INC regularization min_samples_leaf
- visualize errors


6. Write a Custom Scorer for Precision@90% Recall
metrics = accuracy BUT

fraud detection or medical diagnosis = recall target
while maximizing precision = critical

predict_proba
make_scorer for use in GridSearchCV or cross_val_score

NB: example did not like needs_threshold=True - so removed
#scorer = make_scorer(precision_at_recall_90, needs_threshold=True)

Precision at 90% Recall: 0.2960
Best Params: {'max_depth': 3, 'n_estimators': 50}


5. Why Does PCA Before Regression Sometimes Hurt Performance?
PCA projects data to directions of maxiumum variance ignoring target variable

R² without PCA: 0.5758              usually higher PCA discard low-variance features
R² with PCA: 0.4329                 lower - PCA does not consider target variable


4. Implement Early Stopping for GradientBoostingClassifier