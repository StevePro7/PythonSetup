import asyncio

async def fetch_item(item: str) -> None:
    await asyncio.sleep(1)
    print(f"Fetched {item}")

async def main():
    items = ['potion', 'scroll', 'wand']
    for item in items:
        await fetch_item(item)

asyncio.run(main())
