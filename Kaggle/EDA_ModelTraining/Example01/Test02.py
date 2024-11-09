import pandas as pd

# Step 1: Loading and Understanding the Data
data = pd.read_csv('diabetes.csv')
#data.head()
#data.info()


# Step 2: Conducting Exploratory Data Analysis (EDA) and Data Visualization
#data.describe()

# Step 2.2: visualizing data distributions
import matplotlib.pyplot as plt

# Histogram of a specific column
# data['Glucose'].hist(bins=30)
# plt.xlabel('Glucose')
# plt.ylabel('Frequency')
#plt.title('Distribution of Glucose')
#plt.show()


# Step 3: Correlations
import seaborn as sns
# plt.figure(figsize=(10, 8))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
#plt.title('Glucose correlations')
#plt.show()


# Step 4: checking relationships
# plt.scatter(data['Pregnancies'], data['Glucose'], c=data['Outcome'])
# plt.xlabel('Pregnancies')
# plt.ylabel('Glucose')
# plt.title('Pregnancies vs. Glucose')
#plt.show()

# pair plot
#sns.pairplot(data, hue='Outcome')
#plt.show()

# visualizing missing values
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Missing values heatmap')
plt.show()
