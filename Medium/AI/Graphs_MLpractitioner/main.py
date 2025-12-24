import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set up the figure
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
fig.canvas.manager.set_window_title("Graphs Demo")
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 1. Histogram (Skew vs Log)
data_skewed = np.random.exponential(scale=2, size=1000)
data_log = np.log(data_skewed)
sns.histplot(data_skewed, kde=True, ax=axes[0, 0], color='salmon')
axes[0, 0].set_title("1. Skewed Distribution (Raw)")
axes[0, 0].set_xlabel("Glucose Level")

# 2. Box Plot (Class Separation)
class_0 = np.random.normal(30, 5, 100)
class_1 = np.random.normal(60, 5, 100)
axes[0, 1].boxplot([class_0, class_1], labels=['Healthy', 'Diabetic'])
axes[0, 1].set_title("2. Class Separation (Good Feature)")

# 3. Heatmap (Correlation)
corr_matrix = np.array([[1.0, 0.98],
                        [0.98, 1.0]])
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[0, 2], cbar=False)
axes[0, 2].set_title("3. Redundant Features (Correlation)")
axes[0, 2].set_xticklabels(['BMI', 'Weight'])
axes[0, 2].set_yticklabels(['BMI', 'Weight'])

# 4. Scatter Plot (Non-linear)
x = np.linspace(-10, 10, 100)
loc = 0     # mean
scale = 10  # std dev
size = 100  # no. random numbers
# normal = normal distribution = bell curve
y = x ** 2 + np.random.normal(loc=loc, scale=scale, size=size)
axes[1, 0].scatter(x, y, alpha=0.6)
axes[1, 0].set_title("4. Nonlinear Pattern (U-Shape)")

# 5. ROC vs PR Curve (Stylized)
axes[1, 1].plot([0, 0, 1], [0, 1, 1], label='ROC (Looks Good)', color='green', lw=2)
axes[1, 1].plot([0, 1], [1, 0.1], label='PR (Looks Weak)', color='red', linestyle='--', lw=2)
axes[1, 1].legend()
axes[1, 1].set_title("5. ROC vs PR (Imbalanced Data)")

# 6. Learning Curve (High Variance)
start = 10
stop = 100
num = 10
train_sizes = np.linspace(start=start, stop=stop, num=num)
train_err = np.zeros(10) + 0.1
val_err = np.linspace(0.8, 0.6, 10) # Gap remains large
axes[1, 2].plot(train_sizes, train_err, label='Training Error', color='blue')
axes[1, 2].plot(train_sizes, val_err, label='Validation Error', color='orange')
axes[1, 2].fill_between(train_sizes, train_err, val_err, color='gray', alpha=0.1)
axes[1, 2].text(50, 0.4, "Large Gap = Overfitting", fontsize=10)
axes[1, 2].set_title("6. Learning Curve (High Variance)")
axes[1, 2].legend()


plt.show()