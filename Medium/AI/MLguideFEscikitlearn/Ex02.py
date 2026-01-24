import pandas as pd
from datetime import datetime
from info import df

# Assume today = 19-Sep-2025
today = datetime.strptime("2025-09-19", "%Y-%m-%d")

# Convert to datetime and calculate days since last login
df["last_login_date"] = pd.to_datetime(df["last_login_date"])
df["days_since_last_login"] = (today - df["last_login_date"]).dt.days
print(df[["last_login_date", "days_since_last_login"]].head())