# 04. Sample function sample()
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Read and display the random 10 rows from the dataset
print(df.sample(10))