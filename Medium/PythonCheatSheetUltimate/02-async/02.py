import asyncio
from utils import fetch_data

async def main():
    await fetch_data()

asyncio.run(main())
