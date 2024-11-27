import asyncio

async def async_task():
    print("Task beg")
    await asyncio.sleep(1)
    print("Task end")