# Ex01
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer

# Load the dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
target_names = cancer.target_names
print(f"Original data shape: {X.shape}")
# Original data shape: (569, 30)

# Ex02
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)