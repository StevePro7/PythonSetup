import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Calculate correlation with target
correlation_with_target = df.corr()["target_column"].sort_values(ascending=False)
print(correlation_with_target)

# Visualize
correlation_with_target[1:].plot(kind='barh')
plt.title('Feature Correlation with Target')
plt.show()
