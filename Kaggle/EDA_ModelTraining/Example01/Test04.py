import pandas as pd

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')

# Step 4: Feature Selection and Engineering
# example using correlation thresold for feature selection
correlation_matrix = data.corr()
high_corr = correlation_matrix.index[abs(correlation_matrix['Outcome']) > 0.5]
data = data[high_corr]

print(data)
print("data end")