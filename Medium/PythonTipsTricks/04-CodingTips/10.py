# 10. Functional programming techniques: map()
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)

print()
# Condensed way: using map()
squared2 = list(map(lambda x: x ** 2, numbers))
print(squared2)