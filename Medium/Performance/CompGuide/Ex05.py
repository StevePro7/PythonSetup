import timeit


def list_lookup(n):
    names = [f"person_{i}" for i in range(n)]
    ages = list(range(n))
    return ages[names.index("person_999999")]


def dict_lookup(n):
    age_dict = {f"person_{i}": i for i in range(n)}
    return age_dict["person_999999"]


print("List lookup:", timeit.timeit(lambda: list_lookup(1000000), number=100))
print("Dict lookup:", timeit.timeit(lambda: dict_lookup(1000000), number=100))