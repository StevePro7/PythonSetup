import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 25, 30]
})

print(df.head())
print()

print(df.tail())
print()

print(df.info())
print()

print(df.describe())
print()