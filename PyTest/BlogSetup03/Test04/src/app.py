import asyncio

async def fetch_data():
    # Simulate I/O operation.
    await asyncio.sleep(1)
    return {"status": "OK", "data": [42]}
