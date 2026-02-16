from my_api_py import Container

print("beg")

container = Container(10)

for i in range(0, 10):
    container[i] = i


for i in range(0, 10):
    print(container[i])


print("end")