# 15. enumerate(): cleaner looping with indices
items = ['apple', 'banana', 'cherry']
for i in range(len(items)):
    print(f"Item {i+1}: {items[i]}")
print()

# Condensed way: using enumerate()
for i, item in enumerate(items):
    print(f"Item {i+1}: {item}")
