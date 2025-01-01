# 03. Data Normalization
import numpy as np

# Sample dataset
data = np.array([[2.5, 3.0], [1.0, 4.0], [3.5, 5.0]])

# Normalize data (min-max scaling)
data_min = np.min(data, axis=0)
data_max = np.max(data, axis=0)
normalized_data = (data - data_min) / (data_max - data_min)

print("Normalized Data:")
print(normalized_data)