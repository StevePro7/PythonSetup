import asyncio

print('beg')

async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello async world")

async def do_something_else():
    print("Starting another task")
    await asyncio.sleep(1)
    print("finish another task")


async def main():
    await asyncio.gather(
        say_hello_async(),
        do_something_else()
    )

asyncio.run(main())
print('end')