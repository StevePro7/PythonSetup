import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import operator

x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)

x = x[:, np.newaxis]
y = y[:, np.newaxis]

polynomial_features3= PolynomialFeatures(degree=4)
x_poly3 = polynomial_features3.fit_transform(x)
model3 = LinearRegression()
model3.fit(x_poly3, y)
y_poly_pred3 = model3.predict(x_poly3)

rmse3 = np.sqrt(mean_squared_error(y,y_poly_pred3))
r23 = r2_score(y,y_poly_pred3)
#print(rmse3)
#print(r23)

plt.scatter(x, y, s=10)

import operator
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred3), key=sort_axis)
x, y_poly_pred3 = zip(*sorted_zip)
plt.plot(x, y_poly_pred3, color='m')
plt.show()