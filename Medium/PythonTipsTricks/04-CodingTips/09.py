# 09. Merging dictionaries: cleaner merging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)

print()
# Condense way: dictionary merge operator
# Python 3.9
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict2 = dict1 | dict2
print(merged_dict2)

# ERROR for me!
# Python 3.8.10
# TypeError: unsupported operand type(s) for |: 'dict' and 'dict'