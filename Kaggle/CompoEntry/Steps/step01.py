import pandas as pd

class Step01:

    def __init__(self):
        self.data = None
        self.df = None

    def read_csv(self, filepath: str):
        self.data = pd.read_csv(filepath)
        self.df = self.data.copy(deep=True)

