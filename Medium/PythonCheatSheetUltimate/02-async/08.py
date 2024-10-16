import asyncio

async def risky_spell():
    await asyncio.sleep(1)
    raise ValueError("The spell backfired!")

async def main():
    try:
        await risky_spell()
    except ValueError as e:
        print(f"Caught an error: {e}")

asyncio.run(main())
