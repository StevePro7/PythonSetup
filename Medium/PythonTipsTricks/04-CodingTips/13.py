# 13. Using itertools: streamline complex iterations
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = []

for x in list1:
    for y in list2:
        pairs.append((x, y))

print(pairs)
print()

# Condensed way: using itertools.product
from itertools import product
pairs2 = list(product(list1, list2))
print(pairs2)
