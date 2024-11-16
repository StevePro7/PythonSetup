import numpy as np
import pandas as pd


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