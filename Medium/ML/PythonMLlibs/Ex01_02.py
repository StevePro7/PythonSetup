# 2. MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='Sine Wave', color='green', linestyle='-', linewidth=2)
# plt.title("Sine Wave")
# plt.xlabel("X Axis ")
# plt.ylabel("Y Axis ")
# plt.legend()
# plt.grid(True)
#plt.show()

# Bar plot
categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
popularity = [85, 70, 60, 90, 50]

# plt.figure(figsize=(7, 4))
# plt.bar(categories, popularity, color='teal')
# plt.title("Programming Language Popularity")
# plt.xlabel("Languages")
# plt.ylabel("Popularity (%)")
# plt.show()

# Histogram
data = np.random.randn(1000)

# plt.figure(figsize=(7, 4))
# plt.hist(data, bins=30, color='skyblue', edgecolor='black')
# plt.title("Histogram of Normally Distributed Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# Scatter plot
x=np.random.randn(50)
y=np.random.randn(50)
colors=np.random.rand(50)
sizes=1000 * np.random.rand(50)

# plt.figure(figsize=(6, 6))
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
# plt.title("Scatter Plot of Random Points")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.colorbar()
# plt.show()

# Pie chart
labels = ['Apple', 'Banana', 'Mango', 'Pineapple']
sizes = [30, 25, 25, 20]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# plt.figure(figsize=(6, 6))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True)
# plt.title("Fruit Distribution")
# plt.axis('equal')
# plt.show()