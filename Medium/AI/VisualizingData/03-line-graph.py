import matplotlib.pyplot as plt


# Monthly sales figures over six months.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 120, 150, 170, 160, 180]

plt.plot(months, sales, marker='o', linestyle='-', color='blue')

plt.title('Monthly Sales Over Time')

plt.xlabel('Month')
plt.ylabel('Sales ($)')

plt.grid(True) # Gridlines are added for better readability.

plt.show()