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

# Usage
api_key = "demo"
apple_data = get_stock_data("AAPL", "2024-01-01", "2024-09-31", api_key)
print(apple_data.head())