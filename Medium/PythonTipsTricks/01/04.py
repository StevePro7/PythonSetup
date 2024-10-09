import sys

lst1 = [i for i in range(10000)] # list comprehension
lst2 = (i for i in range(10000)) # generator comprehension

print(sum(lst1))
print(sum(lst2))


print(sys.getsizeof(lst1, "bytes"))
print(sys.getsizeof(lst2, "bytes"))
