import asyncio
from utils import fetch_data

async def main():
    task1 = fetch_data()
    task2 = fetch_data()
    await asyncio.gather(task1, task2)

asyncio.run(main())
