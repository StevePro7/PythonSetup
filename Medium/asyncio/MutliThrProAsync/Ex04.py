# 04. - AsyncProgramming
import asyncio


async def fetch_data(delay, name):
    print(f"Task {name}: Started")
    await asyncio.sleep(delay)
    print(f"Task {name}: Completed after {delay} seconds")
    return f"Data from {name}"


async def main():
    # Create tasks
    task1 = asyncio.create_task(fetch_data(2, 'A'))
    task2 = asyncio.create_task(fetch_data(3, 'B'))
    task3 = asyncio.create_task(fetch_data(1, 'C'))

    # Wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)
    print("All tasks completed")
    for result in results:
        print(result)


# Run the main coroutine
asyncio.run(main())