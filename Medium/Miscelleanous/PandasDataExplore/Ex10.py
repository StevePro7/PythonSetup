# 10. Unique function unique()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display all unique values in a column.
print(df["Category"].unique())