# Correlation matrix example
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix

# Sample dataset
data = {
    'Age': [23, 45, 31, 35, 40, 50, 38, 29],
    'Income': [50000, 120000, 75000, 80000, 95000, 110000, 85000, 65000],
    'Education_Level': [2, 4, 3, 4, 5, 4, 3, 2],
    'Experience_Years': [1, 20, 8, 10, 15, 18, 12, 5]
}

df = pd.DataFrame(data)
print(df)

# Calculate the correlation matrix
corr_matrix = df.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.show()


print('the end')