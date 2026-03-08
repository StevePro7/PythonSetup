import asyncio, time

async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    start = time.time()
    result1 = await fetch_data("https://api1.com")
    result2 = await fetch_data("https://api2.com")
    result3 = await fetch_data("https://api3.com")
    end = time.time()
    print(f"Total time: {end - start:.2f}s")

asyncio.run(main())
# Total time: 6.04s
