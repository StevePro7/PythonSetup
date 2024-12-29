import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import requests
import pandas as pd

def get_stock_data(symbol, start_date, end_date, api_key):
    url = f"https://eodhistoricaldata.com/api/eod/{symbol}"
    params = {
        "from": start_date,
        "to": end_date,
        "api_token": api_key,
        "fmt": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = pd.DataFrame(response.json())
        data['date'] = pd.to_datetime(data['date'])
        return data.set_index('date')
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def prepare_data(df, look_back=30):
    X, y = [], []
    for i in range(len(df) - look_back):
        X.append(df.iloc[i:i+look_back]['close'].values)
        y.append(df.iloc[i+look_back]['close'])
    return np.array(X), np.array(y)

#loading data
api_key = "demo"
apple_data = get_stock_data("AAPL", "2024-01-01", "2024-09-31", api_key)
print(apple_data.head())

# Prepare data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(apple_data[['close']])

X, y = prepare_data(pd.DataFrame(scaled_data, columns=['close']))
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(30, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, batch_size=32, epochs=100)

print("Model trained successfully")