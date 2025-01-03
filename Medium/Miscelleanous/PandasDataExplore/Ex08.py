# 08. Shape attribute
import pandas as pd

# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")

# Display the number of rows and columns in the dataset
print(df.shape)