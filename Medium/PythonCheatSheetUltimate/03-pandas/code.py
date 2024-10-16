import pandas as pd

# 01
data = {
    'Element': ['Earth', 'Water', 'Fire', 'Air'],
    'Symbol': ['🜃', '🜄', '🜂', '🜁']
}
df = pd.DataFrame(data)
print(df)


# 02
# df = pd.read_csv('elements.csv')


03.
print(df.head())


04.
symbols = df['Symbol']
print(symbols)


05.
fire_elements = df[df['Element'] == 'Fire']
print(fire_elements)


06.
df['Length'] = df['Element'].apply(len)
print(df['Length'])


07.
element_groups = df.groupby('Element').agg({'Length': 'mean'})
print(element_groups)


08.
df2 = pd.DataFrame({'Element': ['Earth', 'Fire'], 'Quality': ['Solid', 'Plasma']})
merged_df = pd.merge(df, df2, on='Element')
print(merged_df)


09.
df.fillna(value='Unknown', inplace=True)
print(df)


10.
pivoted_df = df.pivot(index='Element', columns='Symbol', values='Length')