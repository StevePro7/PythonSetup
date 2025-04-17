def my_generator():
    yield 1
    yield 2
    yield 3


for item in my_generator():
    print(item)