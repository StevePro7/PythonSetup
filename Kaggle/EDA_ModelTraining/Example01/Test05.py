import pandas as pd

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')

# Step 5: Model Selection and Training with Scikit-Learn
# splitting the data: divide data into training and test sets

from sklearn.model_selection import train_test_split
X = data.drop('Outcome', axis=1)
y = data['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# choose an algortihm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# models = {
#     "Logistic Regression": LogisticRegression(),
#     "Random Forest": RandomForestClassifier(),
#     "SVM": SVC()
# }
#
# results = {}
# for model_name, model in models.items():
#     model.fit(X_train, y_train)
#     results[model_name] = model.score(X_test, y_test)
#
# print(results)

# evaluating model performance
# evaluate each model with metrics: accuracy, precision, recall [F1-score]
from sklearn.metrics import classification_report

#model = RandomForestClassifier()
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("beg")
print(classification_report(y_test, y_pred))
print("end")