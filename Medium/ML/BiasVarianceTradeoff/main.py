import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create dataset
np.random.seed(42)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel() + 0.3 * np.random.randn(40)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

degrees = [1, 3, 10]  # low, medium, high complexity

plt.figure(figsize=(15, 4))
for i, d in enumerate(degrees):
    poly = PolynomialFeatures(degree=d)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_poly_train, y_train)

    y_train_pred = model.predict(X_poly_train)
    y_test_pred = model.predict(X_poly_test)

    train_error = mean_squared_error(y_train, y_train_pred)
    test_error = mean_squared_error(y_test, y_test_pred)

    plt.subplot(1, 3, i + 1)
    plt.scatter(X_train, y_train, color='blue', label='Train')
    plt.scatter(X_test, y_test, color='red', label='Test')
    X_plot = np.linspace(0, 5, 100).reshape(-1, 1)
    plt.plot(X_plot, model.predict(poly.transform(X_plot)), color='green', label='Model')
    plt.title(f'Degree={d}\nTrain MSE={train_error:.2f}, Test MSE={test_error:.2f}')
    plt.legend()

plt.show()