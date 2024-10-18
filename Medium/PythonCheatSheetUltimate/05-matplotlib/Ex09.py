import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'Five'])
plt.yticks([0, 5, 10, 15, 20, 25], ['0', '5', '10', '15', '20', '25+'])
plt.show()