# 5. Get Unique Elements from a List while Preserving Order
lst = [2, 4, 4, 6, 6, 6, 8, 8, 8, 8]
unique_ordered = list(dict.fromkeys(lst))
print(unique_ordered)
