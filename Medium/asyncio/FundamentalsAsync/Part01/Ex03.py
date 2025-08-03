import asyncio


async def simple_coroutine():
    await asyncio.sleep(1)
    return "Coroutine result"

coro = simple_coroutine()
print(f"info: {type(coro)}")


async def runner():
    result = await simple_coroutine()
    print(result)


#asyncio.run(runner())