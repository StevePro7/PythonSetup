from memory_profiler import profile

@profile
def mem_hung_func() -> None:
    big = [i for i in range(100000)]
    del big


mem_hung_func()