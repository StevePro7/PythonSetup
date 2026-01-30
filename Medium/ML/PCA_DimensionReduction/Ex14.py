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

# Ex03
# Initialize PCA to reduce to 2 components
pca = PCA(n_components=2)

# Fit and transform the scaled data
X_pca = pca.fit_transform(X_scaled)
print(f"Data shape after PCA: {X_pca.shape}") # (569 samples, 2 components)
# Data shape after PCA: (569, 2)

# Ex04.
# Check the explained variance ratio
explained_variance = pca.explained_variance_ratio_
print(f"Explained variance by PC1: {explained_variance[0]:.2f}") # e.g., 0.44
print(f"Explained variance by PC2: {explained_variance[1]:.2f}") # e.g., 0.19
print(f"Total explained variance by 2 components: {np.sum(explained_variance):.2f}") # e.g., 0.63
# Explained variance by PC1: 0.44
# Explained variance by PC2: 0.19
# Total explained variance by 2 components: 0.63