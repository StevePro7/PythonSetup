import asyncio

async def task1():
    print(f"start task 1")
    await asyncio.sleep(3)
    print(f"-end- task 1")


async def task2():
    print(f"start task 2")
    await asyncio.sleep(2)
    print(f"-end- task 2")

async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())