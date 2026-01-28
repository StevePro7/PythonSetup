# 2. PANDAS
import pandas as pd

# time-series analysis: resample + rolling window
dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame({'value': [1,2,3,4,5,6]}, index=dates)
# resample weekly sum
#print(df.resample('W').sum())

# rolling mean with window=3
#print(df.rolling(window=3).mean())

# multi-index slicing + manipulation
arrays = [['a','a','b','b'], [1,2,1,2]]
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
df = pd.DataFrame({'data':[10,20,30,40]}, index=index)
#print(df.loc['a'])

# efficient categorical data operations
df = pd.DataFrame({'col': ['foo', 'bar', 'foo', 'bar']*10000})
df['col'] = df['col'].astype('category')
print(df.memory_usage(deep=True))