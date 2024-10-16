import asyncio

async def guarded_spell(semaphore: asyncio.Semaphore, item: int) -> None:
    async with semaphore:
        print(f"Processing {item}")
        await asyncio.sleep(1)

async def main() -> None:
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(guarded_spell(semaphore, i) for i in range(3)))

asyncio.run(main())
