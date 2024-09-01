#set_ex = {1, 2, 3}
#dict_obj = {set_ex: "This is a Set"}
#TypeError: unhashable type: 'set'

set_ex = frozenset({1, 2, 3})
dict_obj = {set_ex: "This is a Set"}
print(dict_obj[set_ex])
#OUTPUT
#This is a Set