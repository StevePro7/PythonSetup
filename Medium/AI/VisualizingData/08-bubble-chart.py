import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(20)
y = np.random.rand(20)

sizes = np.random.rand(20) * 500 # extra variable

plt.scatter(x, y, s=sizes, alpha=0.5, color='magenta')

plt.title('Bubble Chart Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
