from sklearn.preprocessing import KBinsDiscretizer
from info import df

# We need to reshare the data for the transformer
tenure_data = df[["tenure_months"]]

# Initialize the binner to create 3x groups
binner = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="uniform", subsample=None)

# Fit and transform the data
df["tenure_group"] = binner.fit_transform(tenure_data)

print(df[["tenure_months", "tenure_group"]].head())
