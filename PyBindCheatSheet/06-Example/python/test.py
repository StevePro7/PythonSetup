from my_api_py import Container

container = Container(10)

for i in range(0, 10):
    container[i] = i
    result: str = f"Container[{i}] = {container[i]}"
    print(result)
