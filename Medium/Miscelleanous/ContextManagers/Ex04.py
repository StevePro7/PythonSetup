import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer():
    print("Starting async timer")
    start = asyncio.get_event_loop().time()
    yield
    end = asyncio.get_event_loop().time()
    print(f"Elapsed time: {end - start:.4f} seconds")

async def main():
    async with async_timer():
        await asyncio.sleep(1)

asyncio.run(main())


# OUTPUT
# Starting async timer
# Elapsed time: 1.0150 seconds