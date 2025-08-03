import asyncio
import time


async def fetch_data(source):
    """
    """
    print(f"BEG {source}")
    await asyncio.sleep(2)
    print(f"end {source}")


async def main():
    start = time.time()

    results = await asyncio.gather(
        fetch_data("API #1"),
        fetch_data("API #2"),
        fetch_data("API #3")
    )

    print(f"Total: {time.time()-start:.2f}")


if __name__ == '__main__':
    asyncio.run(main())
