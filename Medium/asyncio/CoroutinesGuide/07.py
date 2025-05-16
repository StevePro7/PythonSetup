import asyncio

async def my_coroutine():
    print("Start coroutine")
    await asyncio.sleep(1)
    print("-end- coroutine")


asyncio.run(my_coroutine())