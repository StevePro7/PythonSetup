# 05. Avoid mutable default args
def add_item1(item, items=[]):
    items.append(item)
    return items

print(add_item1('foo'))
print(add_item1('bar'))


# Correct way: using None as a Default
print()
def add_item2(item, items: list=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item2('foo'))
print(add_item2('bar'))
