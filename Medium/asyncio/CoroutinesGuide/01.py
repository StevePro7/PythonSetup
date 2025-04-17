import asyncio

async def my_coroutine():
    print("Hello from coroutine")

x = my_coroutine()
#print(x)

asyncio.run(x)