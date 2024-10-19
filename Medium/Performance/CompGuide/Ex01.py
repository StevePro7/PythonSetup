import cProfile

def slow_func() -> int:
    tot = 0
    for i in range(1000000):
        tot += i
    return tot


def main():
    res = slow_func()
    print(f"{res}")


cProfile.run('main()')