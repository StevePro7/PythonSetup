import pandas as pd

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')

print('data head')
print(data.head())

print('data info')
#data.info()

print('data describe')
#print(data.describe())
print('data end')