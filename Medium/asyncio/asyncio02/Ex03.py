import asyncio

async def fetch_data(data_id: int) -> None:
    print(f'Fetching data for ID {data_id}')
    await asyncio.sleep(3)  # Simulates waiting for a response from a server
    print(f'Finished fetching data for ID {data_id}')

async def main() -> None:
    await fetch_data(1)
    await fetch_data(2)
    await fetch_data(3)

asyncio.run(main())