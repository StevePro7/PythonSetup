import httpx
import asyncio
import time

url = 'https://www.leapcell.io'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

async def make_request(client):
    response = await client.get(url, headers=headers)
    print(response.status_code)

async def main():
    num: int = 3
    async with httpx.AsyncClient() as client:
        start = time.time()
        tasks = [asyncio.create_task(make_request(client)) for _ in range(num)]
        await asyncio.gather(*tasks)
        end = time.time()
        print(f'sent {num} requests, cost: {end - start}')

if __name__ == '__main__':
    asyncio.run(main())
