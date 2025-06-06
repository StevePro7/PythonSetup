import asyncio
import aiohttp

url = 'https://www.leapcell.io'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

async def main():
    async with aiohttp.ClientSession() as client:
        async with client.get(url, headers=headers) as response:
            print(await response.text())
            print(response.status)

if __name__ == '__main__':
    asyncio.run(main())
