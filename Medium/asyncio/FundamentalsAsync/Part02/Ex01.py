import asyncio

async def limited_operation(semaphore, task_id):
    async with semaphore:
        print(f"Task {task_id} semaphore acquired")
        await asyncio.sleep(2)
        print(f"Task {task_id} semaphore released")
        return f"Result {task_id}"

async def demo_semaphore():
    sempaphore = asyncio.Semaphore(2)

    tasks = [
        limited_operation(sempaphore, i)
        for i in range(5)
    ]

    results = await asyncio.gather(*tasks)
    return results

asyncio.run(demo_semaphore())