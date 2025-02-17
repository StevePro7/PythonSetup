import numpy as np
import matplotlib.pyplot as plt


data = np.random.uniform(1.30, 2.10, size=1000)

plt.hist(data, bins=10, color='green', edgecolor='black')

plt.title("Brazil Men's Height Distributions")

plt.xlabel('Height')
plt.ylabel('Frequency')

plt.show()
