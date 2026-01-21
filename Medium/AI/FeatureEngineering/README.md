You’re Not Bad at Machine Learning — Your Features Are
21-Jan-2026

https://medium.com/@rohanmistry231/youre-not-bad-at-machine-learning-your-features-are-815b3f1db6b0


uv add
pandas
numpy
matplotlib
scikit-learn
shap
ipython


Create new features

# Date-based features
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
# Interaction features
df['age_x_income'] = df['age'] * df['income']
df['price_per_unit'] = df['total_price'] / df['quantity']

# Categorical encoding
df['category_encoded'] = pd.factorize(df['category'])[0]

# Binning continuous variables
df['age_bin'] = pd.cut(df['age'], bins=[0, 25, 50, 75, 100])

# Log transformation (for skewed distributions)
df['log_price'] = np.log1p(df['price'])
print(df.head())
