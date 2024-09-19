import asyncio

async def fetch_data(data_id: int) -> None:
    print(f'Fetching data for ID {data_id}')
    await asyncio.sleep(3)  # Simulates waiting for a response from a server
    print(f'Finished fetching data for ID {data_id}')

async def main() -> None:
    # Create tasks for concurrent execution
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    task3 = asyncio.create_task(fetch_data(3))

    # Await all tasks
    await task1
    await task2
    await task3

asyncio.run(main())