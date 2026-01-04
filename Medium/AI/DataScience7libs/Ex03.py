import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")

sns.set(style="whitegrid")
sns.scatterplot(data=sales, x="date", y="amount")
plt.title("Sales Over Time")
plt.show()