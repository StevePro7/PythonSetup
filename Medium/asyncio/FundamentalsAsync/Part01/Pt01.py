# Pattern 1: Async Data Processing
import asyncio

async def process_item(item):
    print(f"Proc {item}")
    await asyncio.sleep(0.5)
    return f"Proc {item}"

async def process_batch(items):
    tasks = [process_item(item) for item in items]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    items = ["item1", "item2", "item3", "item4", "item5"]
    results = await process_batch(items)

    for result in results:
        print(result)


asyncio.run(main())
