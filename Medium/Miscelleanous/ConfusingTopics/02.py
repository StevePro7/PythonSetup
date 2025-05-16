def add_element(element, my_list=[]):
    my_list.append(element)
    return my_list


print(add_element(1))  # [1]
print(add_element(2))  # [1, 2] (Unexpected!)


def add_element_fix(element, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(element)
    return my_list


print(add_element_fix(1))  # [1]
print(add_element_fix(2))  # [2] (Correct!)