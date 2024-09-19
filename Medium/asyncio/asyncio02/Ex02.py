import asyncio

async def fetch_data(data_id: int) -> str:
    print(f'Fetching data for ID {data_id}')
    await asyncio.sleep(2)  # Simulates a delay like a network request
    print(f'Data fetched for ID {data_id}')
    return f'Data {data_id}'

async def compute_result(value: int) -> int:
    await asyncio.sleep(1)  # Simulates a delay like a computation
    return value * 2

async def process_data() -> None:
    data = await fetch_data(1)
    result = await compute_result(5)
    print(f'Result: {result}')
    print(f'Processed Data: {data}')

asyncio.run(process_data())