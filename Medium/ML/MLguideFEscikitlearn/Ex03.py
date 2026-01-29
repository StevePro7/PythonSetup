# 3. Creating Interaction Features: Combining Clues
from sklearn.preprocessing import PolynomialFeatures
from info import df

# Select the features to interact
interaction_features = df[["tenure_months", "monthly_charge"]]

# Create the interaction terms (e.g. tenure * monthly_charge)
poly = PolynomialFeatures(interaction_only=True, include_bias=False)
interactions = poly.fit_transform(interaction_features)

# Add the new feature to the DataFrame
df["tenure_charge_interaction"] = interactions[:, -1]       # last column = interaction term
print(df[["tenure_months", "monthly_charge", "tenure_charge_interaction"]].head())
