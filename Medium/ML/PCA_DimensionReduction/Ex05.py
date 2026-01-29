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


# Check the explained variance ratio
explained_variance = pca.explained_variance_ratio_
print(f"Explained variance by PC1: {explained_variance[0]:.2f}") # e.g., 0.44
print(f"Explained variance by PC2: {explained_variance[1]:.2f}") # e.g., 0.19
print(f"Total explained variance by 2 components: {np.sum(explained_variance):.2f}") # e.g., 0.63




import matplotlib.pyplot as plt
import numpy as np

# Assuming pca is your PCA model and explained_variance is the explained variance ratio
explained_variance = pca.explained_variance_ratio_

# Calculate the cumulative sum of the explained variance ratio
cumulative_variance = np.cumsum(explained_variance)

# Create a figure and a set of subplots
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# Create a bar chart for the explained variance ratio
ax[0].bar(range(1, len(explained_variance) + 1), explained_variance)
ax[0].set_xlabel('Principal Component')
ax[0].set_ylabel('Explained Variance Ratio')
ax[0].set_title('Explained Variance Ratio of Principal Components')

# Create a line chart for the cumulative sum of the explained variance ratio
ax[1].plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
ax[1].set_xlabel('Number of Principal Components')
ax[1].set_ylabel('Cumulative Explained Variance Ratio')
ax[1].set_title('Cumulative Explained Variance Ratio')

# Layout so plots do not overlap
fig.tight_layout()

plt.show()