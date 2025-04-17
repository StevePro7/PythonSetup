import asyncio

async def say(delay, what):
    print(f"start {what}")
    await asyncio.sleep(delay)
    print(f"-end- {what}")


async def main():
    await say(1, 'hello')
    await say(2, 'world')


asyncio.run(main())