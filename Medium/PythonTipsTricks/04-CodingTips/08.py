# 08. set Operations: simplify membership tests
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for item in list1:
    if item in list2:
        common.append(item)
print(common)
print()

# Condensed way: using sets
# remember sets using curly braces like dicts {}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common2 = set1 & set2
print(common2)
