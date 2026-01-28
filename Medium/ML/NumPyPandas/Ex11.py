import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 25, 30]
})

#print(df["age"])
#print()

#print(df[["name", "age"]])
#print()

#print(df.loc[0])
#name     A
#age     20
#Name: 0, dtype: object

print(df.iloc[0:2])
#  name  age
#0    A   20
#1    B   25