import asyncio

print('beg')

async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello async world")

asyncio.run(say_hello_async())
print('end')