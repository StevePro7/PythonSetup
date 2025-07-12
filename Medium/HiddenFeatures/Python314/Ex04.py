import threading
import time
from concurrent.futures import ThreadPoolExecutor
import sys

def cpu_intensive_task(n, task_id):
    """Simulate CPU-intensive work"""
    result = 0
    for i in range(n):
        result += i ** 2
    return f"Task {task_id}: {result}"

def benchmark_threading(use_free_threading=False):
    """Compare performance with and without GIL"""
    
    if use_free_threading:
        # Enable free-threading mode (GIL disabled)
        sys.set_gil_enabled(False)
        print("Running with GIL disabled")
    else:
        sys.set_gil_enabled(True)
        print("Running with GIL enabled")
    
    start_time = time.time()
    
    # Run CPU-intensive tasks in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(cpu_intensive_task, 1000000, i) 
            for i in range(4)
        ]
        
        results = [future.result() for future in futures]
    
    end_time = time.time()
    print(f"Completed in {end_time - start_time:.2f} seconds")
    return results

# Compare performance
print("=== With GIL (traditional) ===")
benchmark_threading(use_free_threading=False)

print("\n=== Without GIL (free-threading) ===")
benchmark_threading(use_free_threading=True)