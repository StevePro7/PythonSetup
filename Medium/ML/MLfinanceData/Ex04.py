import requests
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta


def get_stock_data(symbol, start_date, end_date, api_key):
    """Fetch stock price data"""
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


def get_sentiment_data(symbol, start_date, end_date, api_key):
    """Fetch sentiment data"""
    url = f"https://eodhistoricaldata.com/api/sentiments?s={symbol}"
    params = {
        "from": start_date,
        "to": end_date,
        "api_token": api_key,
        "fmt": "json"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        symbol_key = f"{symbol}.US"
        if symbol_key not in data:
            raise KeyError(f"No sentiment data found for symbol {symbol}")

        sentiment_df = pd.DataFrame(data[symbol_key])
        sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
        sentiment_df = sentiment_df.set_index('date')

        # Calculate additional sentiment metrics
        sentiment_df['sentiment_strength'] = abs(sentiment_df['normalized'] - 0.5) * 200

        return sentiment_df
    else:
        raise Exception(f"API request failed with status code {response.status_code}")


def prepare_data_with_sentiment(price_df, sentiment_df, look_back=30):
    """Prepare data with both price and sentiment features"""
    # Ensure sentiment_df has same dates as price_df
    combined_df = price_df.join(sentiment_df, how='left')

    # Forward fill sentiment values for missing dates
    combined_df['normalized'] = combined_df['normalized'].ffill()
    combined_df['count'] = combined_df['count'].ffill()
    combined_df['sentiment_strength'] = combined_df['sentiment_strength'].ffill()

    # Fill any remaining NaN values with median values
    combined_df = combined_df.fillna(combined_df.median())

    X, y = [], []
    feature_names = ['close', 'normalized', 'count', 'sentiment_strength']

    for i in range(len(combined_df) - look_back):
        features = []
        for feature in feature_names:
            features.extend(combined_df.iloc[i:i + look_back][feature].values)
        X.append(features)
        y.append(combined_df.iloc[i + look_back]['close'])

    return np.array(X), np.array(y)


# Modified training and prediction code to include dates
def train_model_with_dates(X, y, dates, test_size=0.2):
    """Train model and return results with corresponding dates"""
    # Split the data
    split_idx = int(len(X) * (1 - test_size))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    test_dates = dates[split_idx:]

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)

    return model, X_test, y_test, y_pred, test_dates, score


# Example usage
api_key = "demo"
symbol = "AAPL"
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Get data
stock_data = get_stock_data(symbol, start_date.strftime('%Y-%m-%d'),
                            end_date.strftime('%Y-%m-%d'), api_key)
sentiment_data = get_sentiment_data(symbol, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), api_key)

# Prepare data
X, y = prepare_data_with_sentiment(stock_data, sentiment_data)
dates = stock_data.index[30:]  # Adjust for lookback period

# Train model and get predictions with dates
model, X_test, y_test, y_pred, test_dates, score = train_model_with_dates(X, y, dates)

print(f"Model Score with Sentiment Features: {score:.4f}")

# Calculate error metrics
mse = np.mean((y_test - y_pred) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_test - y_pred))

print(f"Root Mean Square Error: ${rmse:.2f}")
print(f"Mean Absolute Error: ${mae:.2f}")