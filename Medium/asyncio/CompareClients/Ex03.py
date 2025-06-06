import httpx
import asyncio

url = 'https://www.leapcell.io'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

async def main():
    async with httpx.AsyncClient() as client:
        response = httpx.get(url, headers=headers)
        print(response.status_code)

if __name__ == '__main__':
    asyncio.run(main())
