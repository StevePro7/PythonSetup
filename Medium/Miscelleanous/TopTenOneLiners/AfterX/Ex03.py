# 3. Find the Most Frequent Element in a List
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_frequent = max(set(lst), key=lst.count)
print(most_frequent)
