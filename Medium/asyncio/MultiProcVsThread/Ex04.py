import multiprocessing
import time

def square_numbers():
    for i in range(10000000):
        _ = i * i

if __name__ == '__main__':  # Ensures safe process creation on Windows
    processes = [multiprocessing.Process(target=square_numbers) for _ in range(4)]
    start_time = time.time()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing time taken:", time.time() - start_time)