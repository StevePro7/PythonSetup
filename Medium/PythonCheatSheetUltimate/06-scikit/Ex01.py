# 01. Loading a Dataset
from sklearn import datasets


iris = datasets.load_iris()
X, y = iris.data, iris.target