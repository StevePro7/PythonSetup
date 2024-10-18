import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [2, 3, 4, 5, 6]
fig, ax = plt.subplots(2, 1)  # 2 rows, 1 column
ax[0].plot(x, y)
ax[1].plot(x, z)
plt.show()