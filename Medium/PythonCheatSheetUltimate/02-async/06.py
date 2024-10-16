import asyncio
# AttributeError: __aexit__

async def async_context_manager():
    print("Entering context")
    await asyncio.sleep(1)
    print("Exiting context")

async def main():
    async with async_context_manager():
        print("Within context")

asyncio.run(main())
