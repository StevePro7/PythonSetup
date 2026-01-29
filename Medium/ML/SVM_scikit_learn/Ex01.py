import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# 1. Generate Data
np.random.seed(42)
apple_size = np.random.normal(7.5, 0.3, 20)
apple_weight = np.random.normal(180, 10, 20)
orange_size = np.random.normal(8.5, 0.3, 20)
orange_weight = np.random.normal(150, 10, 20)
sizes = np.concatenate([apple_size, orange_size])
weights = np.concatenate([apple_weight, orange_weight])
labels = ["Apple"] * 20 + ["Orange"] * 20

# 2. Combine Data into DataFrame
data = pd.DataFrame({"Size": sizes, "Weight": weights, "Label": labels})

# 3. Train an SVM Classifier
X = data[["Size", "Weight"]]
y = data["Label"]
svm = SVC(kernel='linear', C=1)
svm.fit(X, y)

# 4. Plot Data Points and Decision Boundary
fig, ax = plt.subplots(figsize=(8, 6))
colors = {"Apple": "red", "Orange": "orange"}
for fruit, group in data.groupby("Label"):
    ax.scatter(group["Size"], group["Weight"], color=colors[fruit], label=fruit)

# 5. Decision Boundary
xx, yy = np.meshgrid(np.linspace(6, 10, 500), np.linspace(120, 200, 500))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, levels=[0], linewidths=2, colors="black")
ax.set_title("Fruit Classification with SVM")
ax.set_xlabel("Size (cm)")
ax.set_ylabel("Weight (grams)")
ax.legend()
plt.show()