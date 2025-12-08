# 2. PANDAS
import pandas as pd
import numpy as np

# Handling missing data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'Department': ['HR', 'IT', np.nan, 'Finance', 'IT']
}
df = pd.DataFrame(data)
#print(df)

# Fill missing data with mean
df['Age'].fillna(df['Age'].mean())
#print(df)

# Drop rows with missing values
df_cleaned = df.dropna()
#print(df_cleaned)

# Merging + joining data frames
employees = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
salaries = pd.DataFrame({
    'EmpID': [1, 2, 4],
    'Salary': [50000, 60000, 70000]
})
merged = pd.merge(employees, salaries, on='EmpID', how='left')
#print(merged)

# Pivot tables
data = {
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR'],
    'Gender': ['F', 'M', 'F', 'M', 'F'],
    'Salary': [60000, 52000, 58000, 62000, 54000]
}
df = pd.DataFrame(data)
pivot = pd.pivot_table(df, values='Salary', index='Department', columns='Gender', aggfunc='mean')
#print(pivot)

# Apply + Lambda functions
df = pd.DataFrame({
    'Name': ['alice', 'bob', 'charlie'],
    'Score': [45, 88, 72]
})
df['Name'] = df['Name'].apply(lambda x: x.capitalize())
#print(df)

df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
#print(df)

# Multi-Indexing + Hierarchical data
arrays = [
    ['IT', 'IT', 'HR', 'HR'],
    ['Alice', 'Bob', 'Charlie', 'David']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Department', 'Name'))
df = pd.DataFrame({'Salary': [60000, 65000, 52000, 50000]}, index=index)
#print(df)

# Categorical data + memory optimization
df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance']
})
df['Department'] = df['Department'].astype('category')
#print(df.dtypes)
#Department    category
#dtype: object
