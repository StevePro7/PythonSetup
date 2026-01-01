import numpy as np
import pandas as pd

# Importing and export CSV
# # If all of your columns are the same type:
# x = pd.read_csv('music.csv', header=0).values
# print(x)
#
# # You can also simply select the columns you need:
# x = pd.read_csv('music.csv', usecols=['Artist', 'Plays']).values
# print(x)



a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a)
print(df)
#           0         1         2         3
# 0 -2.582892  0.430148 -1.240820  1.595726
# 1  0.990278  1.171510  0.941257 -0.146925
# 2  0.769893  0.812997 -0.950684  0.117696
# 3  0.204840  0.347845  1.969792  0.519928

df.to_csv('pd.csv')

data = pd.read_csv('pd.csv')
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')