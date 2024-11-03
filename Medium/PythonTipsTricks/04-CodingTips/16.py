# 16. Using any() and all(): simplify condition checking
numbers = [4, 9, 11, 7]
found: bool = False

for number in numbers:
    if number> 10:
        found = True
        break

print(found)
print()

# Condensed way: using any()
found2 = any(number > 10 for number in numbers)
print(found2)