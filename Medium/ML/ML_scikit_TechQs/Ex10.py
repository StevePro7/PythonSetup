import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# Synthetic dataset
np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.2, X.shape[0])

# Function to plot learning curves
def plot_learning_curve(model, X, y, title):
    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y, cv=5, scoring='neg_mean_squared_error',
        train_sizes=np.linspace(0.1, 1.0, 10), random_state=42
    )

    train_errors = -train_scores.mean(axis=1)
    val_errors = -val_scores.mean(axis=1)

    plt.figure(figsize=(8, 5))
    plt.plot(train_sizes, train_errors, label="Training error")
    plt.plot(train_sizes, val_errors, label="Validation error")
    plt.title(title)
    plt.xlabel("Training set size")
    plt.ylabel("MSE")
    plt.legend()
    #plt.show()
    plt.savefig(title + ".png", bbox_inches="tight", dpi=300)
    plt.close()

# Linear Regression (likely high bias)
linear_model = LinearRegression()
plot_learning_curve(linear_model, X, y, "Linear Regression (High Bias)")

# Polynomial Regression (likely high variance)
poly_model = make_pipeline(PolynomialFeatures(degree=10), LinearRegression())
plot_learning_curve(poly_model, X, y, "Polynomial Regression (High Variance)")
