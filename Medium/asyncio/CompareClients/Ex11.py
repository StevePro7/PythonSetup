import time
import asyncio
import aiohttp

url = 'https://www.leapcell.io'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

async def make_request():
    async with aiohttp.ClientSession() as client:
        async with client.get(url, headers=headers) as response:
            print(response.status)

def main():
    num: int = 3
    start = time.time()
    tasks = [asyncio.ensure_future(make_request()) for _ in range(num)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(f'sent {num} requests, cost: {end - start}')

if __name__ == '__main__':
    main()
