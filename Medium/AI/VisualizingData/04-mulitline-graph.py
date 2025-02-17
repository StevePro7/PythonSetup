import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

product_a_sales = [100, 120, 150, 170, 160, 180]
product_b_sales = [90, 110, 130, 160, 150, 170]

plt.plot(months, product_a_sales, marker='o', label='Product A')
plt.plot(months, product_b_sales, marker='s', label='Product B')

plt.title('Product Sales Comparison')

plt.xlabel('Month')
plt.ylabel('Sales ($)')

plt.legend()

plt.grid(True)

plt.show()