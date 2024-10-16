import asyncio

async def fetch_data_01():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate an I/O operation
    print("Data retrieved.")
