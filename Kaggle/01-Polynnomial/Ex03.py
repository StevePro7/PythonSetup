import numpy as np
import sklearn.metrics as metrics

x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)

x = x[:, np.newaxis]
y = y[:, np.newaxis]

mse = metrics.mean_squared_error(x,y)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(x,y)

print('RMSE value:',rmse)
print('R2 value:',r2)
