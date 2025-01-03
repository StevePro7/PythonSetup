# 03. Tail function tail()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the last 10 rows of the dataset
print(df.tail(10))