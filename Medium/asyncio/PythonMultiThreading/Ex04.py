# 6. Thread Pooling
import concurrent.futures

def cube(x):
    print(f'Cube of {x}={x * x * x}')

if __name__ == '__main__':
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(cube, 2)

        # Mas the method 'cube' with a list of values
        result = exe.map(cube, [1, 2, 3, 4, 5])

    for r in result:
        print(r)
