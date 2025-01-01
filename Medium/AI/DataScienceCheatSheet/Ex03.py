# 3. Pandas
import pandas as pd

# Create DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

# Read/Write Data
csv_data = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

# Analyze Data
df.info()
df.describe()

# Filter Rows
filtered_df = df[df['Age'] > 25]

# Grouping
grouped = df.groupby("Name").mean()