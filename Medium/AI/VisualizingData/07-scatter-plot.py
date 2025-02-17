import numpy as np
import matplotlib.pyplot as plt


# explanatory variable (miles per day)
x = [1.5, 1, 3.5, 4, 6, 5, 4, 4.5]
# response variable (weight (kg))
y = [83, 88, 73, 75, 60, 64, 70, 68]

# extra variable (calories ingested per day)
sizes = np.array([4000, 3800, 2700, 2750, 2390, 2400, 2300, 1450]) /10

plt.scatter(x, y, s=sizes, alpha=0.5, color='magenta')

plt.title('Miles(per day) vs Weight (kg)')

plt.xlabel('Miles per Day')
plt.ylabel('Weight (kg)')

plt.grid(True)

plt.show()
