import asyncio, aiohttp
from asyncio import Semaphore

class APIClient:
    def __init__(self, max_concurrent=5):
        self.sem = Semaphore(max_concurrent)

    async def fetch(self, session, uid):
        async with self.sem:   # only N tasks allowed at once
            async with session.get(f"https://api.com/users/{uid}") as resp:
                return await resp.json()

    async def fetch_all(self, uids):
        async with aiohttp.ClientSession() as s:
            tasks = [asyncio.create_task(self.fetch(s, uid)) for uid in uids]
            return await asyncio.gather(*tasks)

client = APIClient(max_concurrent=10)
results = asyncio.run(client.fetch_all(range(50)))