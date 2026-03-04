from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

# Load vectorized 20 Newsgroups dataset
data = fetch_20newsgroups_vectorized(subset='all')
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SGDClassifier (fast, scalable)
sgd = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
start = time.time()
sgd.fit(X_train, y_train)
sgd_time = time.time() - start
sgd_acc = accuracy_score(y_test, sgd.predict(X_test))
print(f"SGDClassifier: Accuracy={sgd_acc:.4f}, Time={sgd_time:.2f}s")

# LogisticRegression (small data, more stable)
logreg = LogisticRegression(max_iter=1000, solver='lbfgs')
start = time.time()
logreg.fit(X_train, y_train)
logreg_time = time.time() - start
logreg_acc = accuracy_score(y_test, logreg.predict(X_test))
print(f"LogisticRegression: Accuracy={logreg_acc:.4f}, Time={logreg_time:.2f}s")

# SGDClassifier: Accuracy=0.8870, Time=1.13s
# LogisticRegression: Accuracy=0.8228, Time=27.17s