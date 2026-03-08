import asyncio

async def greet():
    print("Hello")
    asyncio.sleep(1)
    print("World")

g = greet()
print(g)
# <coroutine object greet at 0x0000029463340700>
