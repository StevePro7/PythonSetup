import asyncio, time

async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    start = time.time()
    task1 = asyncio.create_task(fetch_data("https://api1.com"))
    task2 = asyncio.create_task(fetch_data("https://api2.com"))
    task3 = asyncio.create_task(fetch_data("https://api3.com"))
    results = await asyncio.gather(task1, task2, task3)
    end = time.time()
    print(f"Total time: {end - start:.2f}s")
    print("Results:", results)

asyncio.run(main())
# Total time: 2.01s