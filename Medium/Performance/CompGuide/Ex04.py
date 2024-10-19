import timeit


def list_membership(n):
    my_list = list(range(n))
    return 999999 in my_list


def set_membership(n):
    my_set = set(range(n))
    return 999999 in my_set


print("List membership:", timeit.timeit(lambda: list_membership(1000000), number=100))
print("Set membership:", timeit.timeit(lambda: set_membership(1000000), number=100))