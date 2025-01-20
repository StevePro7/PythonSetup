from tqdm import tqdm
import pandas as pd


tqdm.pandas()

df = pd.DataFrame({"A": range(100)})
df['B'] = df['A'].progress_apply(lambda x: x ** 2)
