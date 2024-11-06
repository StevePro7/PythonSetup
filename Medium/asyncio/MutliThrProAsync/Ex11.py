# 11. - AsyncProgramming
import asyncio

async def limited_task(sem, name):
    async with sem:
        await asyncio.sleep(1)
        print(f"Task {name} completed")

async def main():
    sem = asyncio.Semaphore(3)  # Limit to 3 concurrent tasks
    tasks = [limited_task(sem, i) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())