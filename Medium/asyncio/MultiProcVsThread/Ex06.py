import multiprocessing
import psutil
import os
import time


def memory_usage():
    """Returns the current memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2  # Convert to MB


def cpu_heavy_task(n):
    """Simulates a CPU-heavy task (large sum calculation)"""
    start_memory = memory_usage()

    result = sum(i * i for i in range(n))  # Heavy computation

    end_memory = memory_usage()
    print(f"Process {os.getpid()} | Start: {start_memory:.2f} MB | End: {end_memory:.2f} MB")
    return result


if __name__ == "__main__":
    n = 10_000_000  # Large computation
    num_workers = 4  # Number of parallel processes

    start_time = time.time()

    # Use multiprocessing Pool for efficient process management
    with multiprocessing.Pool(processes=num_workers) as pool:
        pool.map(cpu_heavy_task, [n] * num_workers)

    print(f"Total Execution Time: {time.time() - start_time:.2f} seconds")