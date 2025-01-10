# 3. Find the Most Frequent Element in a List
from collections import Counter


lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_frequent = Counter(lst).most_common(1)[0][0]
print(most_frequent)
