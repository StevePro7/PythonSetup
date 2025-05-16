import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched data from {url}")
        return data


async def main():
    urls = ["https://example.com", "https://python.org", "https://openai.com"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print("Feetched all data")
        print(results)


# Run the main coroutine
asyncio.run(main())