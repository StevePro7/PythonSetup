items = [1, 2, 3, 4, 5, 6]
i = 0
found: bool = False

while i < len(items):
    item = items[i]
    if item == "2":
        found = True
        break
    i += 1

if not found:
    print("call some func")