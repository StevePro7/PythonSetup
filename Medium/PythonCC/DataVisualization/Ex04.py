# 04. Stock Analysis with Moving Avera
import numpy as np

# Simulated daily stock prices
prices = np.array([100, 102, 104, 103, 105, 110, 115])

# Calculate 3-day SMA
window = 3
sma = np.convolve(prices, np.ones(window)/window, mode='valid')

print("3-Day Simple Moving Average:")
print(sma)