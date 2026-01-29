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
print(f"Original data shape: {X.shape}") # (569 samples, 30 features)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize PCA to reduce to 2 components
pca = PCA(n_components=2)
# Fit and transform the scaled data
X_pca = pca.fit_transform(X_scaled)
print(f"Data shape after PCA: {X_pca.shape}") # (569 samples, 2 components)