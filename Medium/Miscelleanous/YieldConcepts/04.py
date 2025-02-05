# def generate_list():
#     return [1, 2, 3, 4, 5]
#
# result = generate_list()
# print(result)  # Output: [1, 2, 3, 4, 5]


def generate_numbers():
    for i in range(1, 5):
        yield i


gen = generate_numbers()
for num in gen:
    print(num)
