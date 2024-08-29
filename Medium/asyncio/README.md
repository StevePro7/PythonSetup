Mastering Python’s Asyncio: A Practical Guide
29-Aug-2024

https://medium.com/@moraneus/mastering-pythons-asyncio-a-practical-guide-0a673265cf04


01.
import time

def say_hello():
    time.sleep(2)
    print("Hello, Async World? (not yet)")

say_hello()



02.
import asyncio

async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async World!")

asyncio.run(say_hello_async())



03.
import asyncio

async def say_hello_async():
    await asyncio.sleep(2)  # Simulates waiting for 2 seconds
    print("Hello, Async World!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulates doing something else for 1 second
    print("Finished another task!")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())



Fetching Web Pages (Concurrent I/O Tasks)
04.
import requests
import time

start_time = time.time()

def fetch(url):
    return requests.get(url).text

page1 = fetch('http://example.com')
page2 = fetch('http://example.org')

print(f"Done in {time.time() - start_time} seconds")

# Output: Done in 0.6225857734680176 seconds



05.
import aiohttp
import asyncio
import time

async def fetch_async(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        page1 = asyncio.create_task(fetch_async('http://example.com', session))
        page2 = asyncio.create_task(fetch_async('http://example.org', session))
        await asyncio.gather(page1, page2)

start_time = time.time()
asyncio.run(main())
print(f"Done in {time.time() - start_time} seconds")

# Output: Done in 0.2990539073944092 seconds



06.
Reading Files (Concurrent I/O Tasks)
# Synchronously reading multiple files
def read_file_sync(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def read_all_sync(filepaths):
    return [read_file_sync(filepath) for filepath in filepaths]

filepaths = ['file1.txt', 'file2.txt']
data = read_all_sync(filepaths)
print(data)


07.
pip install aiofiles

import asyncio
import aiofiles

# Asynchronously reading a single file
async def read_file_async(filepath):
    async with aiofiles.open(filepath, 'r') as file:
        return await file.read()

async def read_all_async(filepaths):
    tasks = [read_file_async(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)

# Running the async function
async def main():
    filepaths = ['file1.txt', 'file2.txt']
    data = await read_all_async(filepaths)
    print(data)

asyncio.run(main())




Mixing Async and Sync: A Hybrid Approach
08.
import asyncio
import time

def sync_task():
    print("Starting a slow sync task...")
    time.sleep(5)  # Simulating a long task
    print("Finished the slow task.")

async def async_wrapper():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_task)

async def main():
    await asyncio.gather(
        async_wrapper(),
        # Imagine other async tasks here
    )

asyncio.run(main())



Future Object
09.
import asyncio

# A function to simulate an asynchronous operation using a Future
async def async_operation(future, data):
    await asyncio.sleep(1)  # Simulate some async work with a delay
    
    # Set the result or exception based on the input data
    if data == "success":
        future.set_result("Operation succeeded")
    else:
        future.set_exception(RuntimeError("Operation failed"))

# A callback function to be called when the Future is done
def future_callback(future):
    try:
        print("Callback:", future.result())  # Attempt to print the result
    except Exception as exc:
        print("Callback:", exc)  # Print the exception if there was one

async def main():
    # Create a Future object
    future = asyncio.Future()
    
    # Add a callback to the Future
    future.add_done_callback(future_callback)
    
    # Start the asynchronous operation and pass the Future
    await async_operation(future, "success")  # Try changing "success" to anything else to simulate a failure
    
    # Check if the Future is done and print its result
    if future.done():
        try:
            print("Main:", future.result())
        except Exception as exc:
            print("Main:", exc)

# Run the main coroutine
asyncio.run(main())