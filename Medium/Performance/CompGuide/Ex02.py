@profile
def slow_func() -> int:
    tot = 0
    for i in range(1000000):
        tot += i
    return tot


slow_func()