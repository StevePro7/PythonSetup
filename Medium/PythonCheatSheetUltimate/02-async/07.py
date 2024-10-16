import asyncio

async def fetch_items():
    items = ['crystal', 'amulet', 'dagger']
    for item in items:
        await asyncio.sleep(1)
        yield item

async def main():
    async for item in fetch_items():
        print(f"Found item {item}")

asyncio.run(main())
