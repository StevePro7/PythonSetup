NumPy + Pandas: The Only Guide You Need
24-Dec-2025

https://medium.com/activated-thinker/numpy-pandas-the-only-guide-you-need-7595c0461b30


uv add numpy pandas


NUMPY
stores array numbers in contiguous memory
all numbers have same data type
operations happen in fast C code
array operations are vectorized = 1 line = 1 million operations


Foundation
PyTorch
Scikit-Learn
TensorFlow


Ex01
Creating NumPy Arrays (3 Functions You’ll Use Forever)
np.array                        → create manually
np.arange(n)                    → 0 to n-1
np.linspace(start, end, count)  → even spacing


Ex02
Shape, Size, Dimensions
shape   → rows x columns
ndim    → number of dimensions
size    → total elements


Ex03
Indexing & Slicing

2D slicing
mat[:, 1]      # entire column 2
mat[1:, :2]    # submatrix

NumPy slicing works like:
rows, columns

remember
columns     n
rows        n - 1


Ex04
Vectorized Operations — NumPy’s Real Magic
powerful because of this:   a + 10
internally uses optimized C loops [not Python loops]

Real ML use:
feature scaling
matrix multiplication


Ex05
Reshaping — MOST Important for ML
Every ML model uses 2D arrays

Reshape NEVER changes data - only the view
Reshape works only if total elements match

Aggregations
a.sum()
a.mean()
a.max()
a.min()

Used daily for:
pre-processing
feature engineering


NUMPY INTERVIEW QUESTIONS

Q1: Why are NumPy arrays faster than Python lists?
Continuous memory
Single data type
Vectorized operations
Uses C behind the scenes


Q2: What is broadcasting?
a = np.array([1,2,3])
b = 5
print(a + b)    # [6 7 8]

Broadcasting
automatically expands dimensions of smaller arrays so
they match the shape of larger arrays during operations
without copying data


Q3: How do you find unique values?
np.unique(arr)


Q4: How do you handle NaN values?
np.isnan(arr)
np.nan_to_num(arr)


PANDAS
Excel + SQL + NumPy combined

Ex10
Understanding Pandas: DataFrame & Series

Series      = single column
DataFrame   = table


Ex11
Selecting Data
Row by label:
df.loc[0]

Row by position:
df.iloc[0:2]


Filtering Rows (Most Common Operation)
Add, Remove Columns

Groupby (Interview Favourite)
* find averages
* count records
* segment customers

Merge / Join (Most Important Real-World Skill)
pd.merge(df1, df2, on="id")


PANDAS INTERVIEW QUESTIONS

Q1: Difference between loc and iloc?
loc indexes based on → label
iloc indexes based on → index number

Q2: How to handle missing values?
df.isna()
df.dropna()
df.fillna(df.mean())

Q3: Why is Pandas slow sometimes?
Because columns may hold Python objects → slower than NumPy.


SUMMARY

NumPy = Fast math + fixed types + big arrays
1. ML math
2. preprocessing
3. matrix operations

Pandas = Smart tables + SQL-like operations
1. EDA
2. data cleaning
3. joining datasets
4. feature engineering