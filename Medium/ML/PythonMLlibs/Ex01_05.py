# 5. SCIPY
import numpy as np
from scipy import linalg, optimize, stats

# Linear Algebra [scipy.linalg]
A = np.array([[3, 2], [1, 4]])

# determinant
det = linalg.det(A)
#print(det)

# inverse
inv_A = linalg.inv(A)
#print(inv_A)

# matrix multiplication
mul = np.dot(A, inv_A)
#print(mul)

# Optimize
def f(x):
    return (x - 3) ** 2

result = optimize.minimize(f, x0=0)
#print(result.x[0])
# Minimum at x = 2.9999999840660854

# Statistics [scipy.stats]
data = np.random.normal(loc=0, scale=1, size=1000)
mean = np.mean(data)
std = np.std(data)

#print(mean)
#print(std)
t_stat, p_value = stats.ttest_1samp(data, popmean=0)
#print(f"T-stat: {t_stat:.3f}, P-value: {p_value:.3f}")

# Integration [scipy.integrate]
from scipy import integrate

result, error = integrate.quad(lambda x: x ** 2, 0, 5)
#print(f"Integral of x^2 from 0 to 5: {result:.2f}")
# Integral of x^2 from 0 to 5: 41.67

# Solving equations [scipy.optimize.root
def equation(x):
    return x ** 2 - 9

sol = optimize.root(equation, x0=1)
#print(f"Root of x^2 - 9 = 0: x = {sol.x[0]}")
# Root of x^2 - 9 = 0: x = 2.9999999999999574
