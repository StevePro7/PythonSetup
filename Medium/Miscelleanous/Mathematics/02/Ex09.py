import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Logistic Regression model
model = LogisticRegression(max_iter=500, solver='lbfgs')
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]


# Visualizing loss for one feature dimension for intuition
coef_range = np.linspace(-2, 2, 100)
losses = []
for coef in coef_range:
    y_prob = 1 / (1 + np.exp(-(X_test[:, 0] * coef)))
    loss = log_loss(y_test, y_prob)
    losses.append(loss)

plt.plot(coef_range, losses, label="Cross-Entropy Loss")
plt.title("Convex Loss Curve for Logistic Regression")
plt.xlabel("Model Coefficient Value")
plt.ylabel("Loss")
plt.legend()
plt.grid()
plt.show()
