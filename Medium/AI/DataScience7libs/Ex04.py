from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

sales = pd.read_csv("sales.csv")

X = sales[["amount"]]
y = sales["category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier().fit(X_train, y_train)
print(model.score(X_test, y_test))
# 1.0