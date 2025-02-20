import threading
import psutil
import os
import time
from concurrent.futures import ThreadPoolExecutor


def memory_usage():
    """Returns the current memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2  # Convert to MB


def io_heavy_task(filename):
    """Reads file in chunks instead of loading everything at once"""
    start_memory = memory_usage()

    with open(filename, "r") as f:
        for _ in f:  # Read line by line to avoid large memory allocations
            pass

    end_memory = memory_usage()
    print(f"Thread {threading.current_thread().name} | Start: {start_memory:.2f} MB | End: {end_memory:.2f} MB")


if __name__ == "__main__":
    # Create a large dummy file
    filename = "large_file.txt"
    with open(filename, "w") as f:
        f.write("Hello, world!\n" * 500_000)  # ~7 MB file

    start_time = time.time()

    # Use a ThreadPoolExecutor to manage threads efficiently
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(io_heavy_task, [filename] * 4)

    print(f"Total Execution Time: {time.time() - start_time:.2f} seconds")