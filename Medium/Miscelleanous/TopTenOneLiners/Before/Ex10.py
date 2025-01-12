# 10. Create a Counter Dictionary from a List
my_list = [1, 3, 3, 5, 5, 5]
counter = {}
for item in my_list:
    counter[item] = counter.get(item, 0) + 1

print(my_list)
print(counter)
