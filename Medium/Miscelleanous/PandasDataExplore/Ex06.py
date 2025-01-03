# 06. Describe function describe()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the basic statistical information about the dataset
print(df.describe())