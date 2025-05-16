a = b = []  # Both a and b point to the same list
a.append(1)
print(b)  # [1] (Unexpected!)


a = []
b = []  # Now they are independent lists
a.append(1)
print(b)  # []