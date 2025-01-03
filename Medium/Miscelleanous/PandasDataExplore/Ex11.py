# 11. Nunique function nunique()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the count of unique values in the dataset, sorted in descending order
result = df.nunique().sort_values(ascending=False)
print(result)