import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Let randomly create some data’s for two variables,

x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
#Visualize the variables spreads for better understanding
plt.scatter(x, y, s=10)
plt.show()