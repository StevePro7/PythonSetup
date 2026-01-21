# Correlation matrix
correlation_matrix = df.corr()

# Features highly correlated with target
target_corr = correlation_matrix["target"].sort_values(ascending=False)

# Remove highly correlated features [multicollinearity]
# if two features have correlation > 0.9 then remove
high_corr_pairs = np.where(
    np.abs(correlation_matrix) > 0.9
)

high_corr_features = set()
for i, j in zip(high_corr_pairs[0], high_corr_pairs[1]):
    if i != j:
        high_corr_features.add(correlation_matrix.columns[j])
print(f"High correlation features to remove: {high_corr_features}")
df = df.drop(columns=high_corr_features)
