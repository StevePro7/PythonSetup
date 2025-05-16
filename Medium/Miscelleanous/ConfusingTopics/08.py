#a, b, c = [1, 2, 3, 4]
#print(a, b, c)  # ValueError! Too many values to unpack


a, *b, c = [1, 2, 3, 4]
print(a, b, c)  # 1 [2, 3] 4