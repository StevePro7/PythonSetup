# 07. Value counts function value_counts()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the count of all unique values in a column,such as "Category"
print(df["Category"].value_counts())