items = [1, 2, 3, 4, 5, 6]
i = 0
found: bool = False

while i < len(items):
    item = items[i]
    if item == "2":
        break
    i += 1
else:
    print("call some func!")