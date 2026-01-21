from scipy.stats import chi2_contingency, f_oneway
import pandas as pd


# Chi-square for categorical features
def chi_square_test(df, categorical_col, target_col):
    contigency_table = pd.crosstab(df[categorical_col], df[target_col])
    chi2, p_value, dof, expected = chi2_contingency(contigency_table)
    return p_value


# ANOVA for continuous features
def anova_test(df, continuous_col, target_col):
    groups = [group[continuous_col].values for name, group in df.groupby(target_col)]
    f_stat, p_value = f_oneway(*groups)
    return p_value


# Calculate p-values for all features
for col in df.columns:
    if col == "target":
        continue
    if df[col].dtype == "object":       # categorical
        p_val = chi_square_test(df, col, "target")
    else:                               # continuous
        p_val = anova_test(df, col, "target")

    print(f"{col}: p-value = {p_val:.4f}")
    # p-value < 0.05 means statistically significant