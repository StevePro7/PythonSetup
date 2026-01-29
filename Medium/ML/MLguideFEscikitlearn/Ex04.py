# 4. Encoding Categories: Making Text Understandable
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from info import df

# We need to reshape the data for the transformer
plan_data = df[["subscription_plan"]]

# Initialize the encoder
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform then create a new DataFrame with the encoded columns
encoded_plans = encoder.fit_transform(plan_data)
encoded_df = pd.DataFrame(encoded_plans, columns=encoder.get_feature_names_out(["subscription_plan"]))

# Join the new encoded columns back to the original DataFrame
df = df.join(encoded_df)
print(df[["subscription_plan_Basic", "subscription_plan_Premium"]])
