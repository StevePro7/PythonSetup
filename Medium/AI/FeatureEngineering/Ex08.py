import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Basic info
print(df.info())        # Data types, missing values
print(df.describe())    # Statistics


# Missing values
missing = df.isnull().sum()
print(f"Missing values:\n{missing}")


# Outliers (for numeric columns)
for col, df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    print(f"{col}: {len(outliers)} outliers")

