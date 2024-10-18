import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [2, 3, 4, 5, 6]
plt.plot(x, y, label='Growth')
plt.plot(x, z, label='Decay')
plt.legend()
plt.show()