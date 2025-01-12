# 5. Get Unique Elements from a List while Preserving Order
def unique_ordered(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


lst = [2, 4, 4, 6, 6, 6, 8, 8, 8, 8]
print(unique_ordered(lst))
