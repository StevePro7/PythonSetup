# 05. Information function info()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display a summary of the dataset
print(df.info())