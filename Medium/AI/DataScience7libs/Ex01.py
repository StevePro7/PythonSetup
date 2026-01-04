import pandas as pd

# Load and clean
sales = pd.read_csv("sales.csv")
sales["date"] = pd.to_datetime(sales["date"], errors="coerce")
sales.dropna(subset=["amount"], inplace=True)

# GroupBy magic
monthly_sales = sales.groupby(pd.Grouper(key="date", freq="ME"))["amount"].sum()
print(monthly_sales)