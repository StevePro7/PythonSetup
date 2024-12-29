from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
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

X, y = prepare_data(apple_data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"Model Score: {model.score(X_test, y_test)}")