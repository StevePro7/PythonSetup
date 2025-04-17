import asyncio

async def main(name):
    print(f"Hello {name}")
    await asyncio.sleep(2)
    print(f"Goodbye {name}")


asyncio.run(main("stevepro"))