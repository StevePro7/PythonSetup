# 05. - AsyncProgramming
import aiohttp
import asyncio

urls = ['http://example.com', 'http://example.org', 'http://example.net']

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result[:100])  # Print the first 100 characters of each result

urls = ['http://example.com', 'http://example.org', 'http://example.net']
asyncio.run(main(urls))