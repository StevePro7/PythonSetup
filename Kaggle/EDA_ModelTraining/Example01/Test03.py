import pandas as pd

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')

# Step 3: Data Preprocessing
data = data.dropna()
#data = data.fillna(method='ffill')

data = pd.get_dummies(data, drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numerical_features = ['BloodPressure', 'BMI']
data[numerical_features] = scaler.fit_transform(data[numerical_features])
