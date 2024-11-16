import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
class Step01:

    def __init__(self):
        self.data = None
        self.df = None

    def read_csv(self, filepath: str):
        self.data = pd.read_csv(filepath)
        self.df = self.data.copy(deep=True)
        self.headers = []
        self.zerocol = {}

    def extract_headers(self):
        for column in self.data:
            self.headers.append(column)

    def head(self, rows: int):
        print(self.data.head(rows))

    def shape(self):
        print(self. data.shape)

    def check_for_nulls(self):
        for header in self.headers:
            zero_sum: int = self.data[header].eq(0).sum()
            self.zerocol[header] = zero_sum
        #print(self.zerocol)

    def replace_zeros(self):
        cols = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]
        self.df[cols] = self.df[cols].replace({'0':np.nan, 0:np.nan})

    def describe(self):
        print(self.df.describe())

    def missing_numbers(self):
        msno.bar(self.df)

    def correlation_matrix(self):
        corr = self.df.corr()
        sns.heatmap(corr, annot=True, square=True)
        #plt.yticks(rotation=0)
        plt.title("Correlation Matrix [heatmap]")
        plt.show()

    def groupby_outcome_line(self):
        self.df.groupby("Outcome").mean().T.plot(figsize=(12, 4))
        plt.title("Group by Outcome [line plot]")
        plt.show()

    def groupby_outcome_bars(self):
        plt.figure(figsize=(20, 10))
        for i, col in enumerate(set(self.df.columns)-{"Outcome"}):
            plt.subplot(2, 4, i + 1)
            #sns.barplot(data=self.df, x="Outcome", y=col, hue=y,    palette=['red','blue'])
            sns.barplot(data=self.df, x="Outcome", y=col, hue="Outcome",)
            sns.color_palette("rocket", as_cmap=True)
            plt.xlabel("Outcome", fontsize = 15)
            plt.xticks(fontsize=10)
            plt.ylabel(col, fontsize=15)
            plt.yticks(fontsize=10)
            plt.set_cmap(plt.get_cmap("hot"))
        plt.show()

