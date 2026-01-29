import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Load dataset from CSV file
df = pd.read_csv('../Data/RELIANCE.csv')

# Convert 'Date' column to datetime and set it as index
df.index = pd.to_datetime(df['Date'])
df = df.drop(['Date'], axis=1)

# Create predictor variables based on price differences
df['Open-Close'] = df['Open'] - df['Close']  # Difference between opening and closing prices
df['High-Low'] = df['High'] - df['Low']  # Difference between high and low prices
X = df[['Open-Close', 'High-Low']]

# Create target variable: 1 if the next day's closing price is higher, else 0
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

# Split data into training (80%) and testing (20%) sets
split_percentage = 0.8
split = int(split_percentage * len(df))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train Support Vector Classifier on training data
cls = SVC().fit(X_train, y_train)

# Predict trading signals for the entire dataset
df['Predicted_Signal'] = cls.predict(X)

# Calculate daily returns based on actual closing prices
df['Return'] = df['Close'].pct_change()

# Calculate strategy returns based on predicted signals
df['Strategy_Return'] = df['Return'] * df['Predicted_Signal'].shift(1)

# Compute cumulative returns for market and strategy
df['Cum_Ret'] = df['Return'].cumsum()  # Cumulative market returns
df['Cum_Strategy'] = df['Strategy_Return'].cumsum()  # Cumulative strategy returns

# Plot cumulative returns for comparison
plt.figure(figsize=(10, 5))
plt.plot(df['Cum_Ret'], color='red', label='Market Returns')
plt.plot(df['Cum_Strategy'], color='blue', label='Strategy Returns')
plt.legend()
plt.title('Trading Strategy Performance')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()