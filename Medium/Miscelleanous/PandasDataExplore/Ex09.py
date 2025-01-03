# 09. Dataframe dtypes attribute
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the data types of all columns
print(df.dtypes)