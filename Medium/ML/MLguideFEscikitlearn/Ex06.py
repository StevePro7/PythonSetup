import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from datetime import datetime
from info import data

# Redefine the original DataFrame to start fresh
df_original = pd.DataFrame(data)

# Assume today = 19-Sep-2025
today = datetime.strptime("2025-09-19", "%Y-%m-%d")

# Convert data column to datetime first as ColumnTransformer works on the data
df_original["last_login_date"] = pd.to_datetime(df_original["last_login_date"])
df_original["days_since_last_login"] = (today - df_original["last_login_date"]).dt.days

# Define the transformers for each column type
# 1. Binner for tenure
# 2. One-Hot Encoder for subscription plan
preprocessor = ColumnTransformer(
    transformers=[
        ("binner", KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="uniform", subsample=None), ["tenure_months"]),
        ("onehot", OneHotEncoder(sparse_output=False), ["subscription_plan"])
    ],
    remainder="passthrough"             # Keep other columns
)

# Create a pipeline that applies the preprocessing
pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

# Apply the entire pipeline to the data
transformed_data = pipeline.fit_transform(df_original)

# The output is a NumPy array
print(transformed_data)
