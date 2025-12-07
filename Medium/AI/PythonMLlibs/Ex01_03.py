# 3. PANDAS
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'Salary': [50000, 60000, 55000, 58000, 62000]
}

df = pd.DataFrame(data)
#print(df)

# DataFrame exploration
#print(df.head(2))
#print(df.tail(2))
#print(df.describe())
#print(df.dtypes)
#print(df.columns)

# Filtering
#print(df[df['Department'] == 'IT'])
#print(df[df['Salary'] > 58000])

# Adding
df['Bonus'] = df['Salary'] * 0.1
#print(df)

df.loc[df['Name'] == 'Bob', 'Age'] == 28
#print(df)

df.drop('Bonus', axis=1, inplace=True)
#print(df)

#print(df.groupby('Department')['Salary'].mean())

# Importing data
#df.to_csv("employees.csv", index=False)

# Exporting data
new_df = pd.read_csv("employees.csv")
print(new_df.head())