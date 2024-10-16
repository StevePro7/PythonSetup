import asyncio

async def perform_spell():
    print("Casting spell...")
    await asyncio.sleep(1)
    print("Spell cast.")

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(perform_spell())
finally:
    loop.close()
