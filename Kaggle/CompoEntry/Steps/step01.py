import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
class Step01:

    def __init__(self):
        self.data = None
        self.df = None
        self.df2 = None

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
            sns.barplot(data=self.df, x="Outcome", y=col, hue="Outcome",)
            sns.color_palette("rocket", as_cmap=True)
            plt.xlabel("Outcome", fontsize = 15)
            plt.xticks(fontsize=10)
            plt.ylabel(col, fontsize=15)
            plt.yticks(fontsize=10)
        plt.show()

    def groupby_outcome_boxs(self):
        plt.figure(figsize=(20, 20))
        for i, col in enumerate(set(self.df.columns)-{"Outcome"}):
            plt.subplot(4, 4, i + 1)
            sns.boxplot(data=self.df, x="Outcome", y=col, hue="Outcome",)
            sns.color_palette("rocket", as_cmap=True)
            plt.xlabel("Outcome", fontsize = 15)
            plt.xticks(fontsize=10)
        plt.show()

    def count_plot(self):
        sns.countplot(x="Outcome", data = self.df, hue="Outcome")
        sns.color_palette("rocket", as_cmap=True)
        plt.show()

    def univariate_plotting(self):
        plt.figure(figsize=(20,25))
        for i, col in enumerate(set(self.df.columns)-{"Outcome"}):
            plt.subplot(6, 4, i+1)
            #sns.distplot(self.df[col])     # deprecated
            sns.histplot(self.df[col], kde=True, stat="density", linewidth=0)
            plt.xlabel(col, fontsize=10)
            plt.xticks(fontsize=10)
        plt.show()

    def replace_distributions(self):
        self.df2 = self.df.copy(deep=True)

        for column in self.df2[["BloodPressure", "BMI"]]:
            self.df2[column] = self.df2[column].fillna(self.df2[column].mean())

        for column in self.df2[["Pregnancies", "Glucose", "DiabetesPedigreeFunction", "Age"]]:
            self.df2[column] = self.df2[column].fillna(self.df2[column].median())
            #self.df2[column] = self.df2[column].fillna(self.df2[column].mean())

    def check_for_outliers(self):
        plt.figure(figsize=(15, 8))
        for i, col in enumerate(set(self.df2.columns)-{"Outcome"}):
            plt.subplot(2, 4, i + 1)
            sns.boxplot(data=self.df2, x=col)
            plt.xlabel(col, fontsize=15)
            plt.xticks(fontsize=10)
        plt.show()

    def detect_outliers(self):
        for col in list(set(self.df2.select_dtypes(include=np.number).columns) - {'Outcome'}):
            q1 = self.df2[col].quantile(0.25)
            q3 = self.df2[col].quantile(0.75)
            iqr = q3 - q1
            low = q1 - (1.5 * iqr)
            high = q3 + (1.5 * iqr)
            n = self.df2.loc[(self.df2[col] < low) | (self.df2[col] > high)].shape[0]

            self.df2.loc[(self.df2[col] < low), col] = low
            self.df2.loc[(self.df2[col] > high), col] = high

