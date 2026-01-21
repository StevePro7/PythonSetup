Evaluating Machine Learning Models: A Guide to Cross-Validation and Performance Metrics
21-Jan-2026

https://christianbernecker.medium.com/evaluating-machine-learning-models-a-guide-to-cross-validation-and-performance-metrics-19c5641af014

uv init --python 3.11.11
uv venv --python 3.11.11

.venv\Scripts\activate
.venv/Scripts/python --version

uv add scikit-learn


Cross Validation
e.g.
K-Fold Cross-Validation

split data set into k parts - called folds
iterate - model trained and evaluated k times
average - final performace = average of the scores from k iterations

Ex01


Confusion Matrix
TP
model correctly predicted +ve class
predict disease and patient sick

TN
model correctly predicted -ve class
predict no disease and patient healthy

FP
model incorrectly predicted +ve class
predicted disease but patient healthy           Type I Error

FN
model incorrectly predicted -ve class
predicted no disease but patient sick           Type II Error


T     correct
F   incorrect

P   +ve class
N   -ve class


PRECISION
purity of +ve predictions

all times model predicted +ve, how often correct?
precision = TP / ( TP + FP )


Recall
completeness of +ve predictions

all actual +ve cases, how many model correctly identify?
recall = TP / ( TP + FN )



F1-Score
balanced metric

harmonic mean of Precision and Recall
f1-score = 2 * ( Precision * Recall ) / ( Precision + Recall ) 


Classification Report
easiest way to see these metrics:
precision, recall, f1-score


SUMMARY
use K-Fold Cross-Validation instead of single train_test_split
to get reliable estimate of model's performance

accuracy not always enough
esp. with imbalanced datasets

understand trade-off between
Precision       minimizing FP
Recall          minimizing FN

use F1-Score when you need balanced measure of model's performance