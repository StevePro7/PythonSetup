import multiprocessing
import time

def compute():
    total = sum(i * i for i in range(10000000))
    print("Computation Done")

processes = [multiprocessing.Process(target=compute) for _ in range(3)]
for process in processes:
    process.start()
for process in processes:
    process.join()