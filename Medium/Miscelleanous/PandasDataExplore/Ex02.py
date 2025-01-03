# 02. Head function head()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the first 10 rows of the dataset
print(df.head(10))