# Pattern 3: Task Creation and Management
import asyncio

async def background_task(name, duration):
    print(f"BG {name} BEG")
    await asyncio.sleep(duration)
    print(f"BG {name} end")
    return f"Task {name}"


async def main():
    task1 = asyncio.create_task(background_task("A", 2))
    task2 = asyncio.create_task(background_task("B", 4))

    print("Do work")
    await asyncio.sleep(0.5)
    print("Work done")

    results = await asyncio.gather(task1, task2)
    print(f"BG results: {results}")


asyncio.run(main())