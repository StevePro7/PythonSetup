# 4. Matplotlib & Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Line Plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Line Plot")
#plt.show()

# Seaborn Heatmap
data = np.random.rand(4, 4)
sns.heatmap(data, annot=True)
plt.show()