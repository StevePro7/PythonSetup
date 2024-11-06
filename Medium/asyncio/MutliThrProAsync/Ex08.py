# 08. - Hybrid
import asyncio
import concurrent.futures
import threading

# Async task
async def async_task():
    await asyncio.sleep(1)
    print("Async task completed")

# CPU-bound task
def cpu_bound_task():
    sum(i * i for i in range(1000000))
    print("CPU-bound task completed")

# I/O-bound task
def io_bound_task():
    with open('example.txt', 'w') as f:
        f.write("Hello, world!")
    print("I/O-bound task completed")

async def main():
    loop = asyncio.get_running_loop()

    # Run async task
    await async_task()

    # Run CPU-bound task in a separate process
    with concurrent.futures.ProcessPoolExecutor() as pool:
        await loop.run_in_executor(pool, cpu_bound_task)

    # Run I/O-bound task in a separate thread
    io_thread = threading.Thread(target=io_bound_task)
    io_thread.start()
    io_thread.join()

asyncio.run(main())