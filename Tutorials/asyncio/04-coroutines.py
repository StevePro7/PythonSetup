import asyncio


async def stuff():
    return 7


@asyncio.coroutine
def py34_coro():
    yield from stuff()


async def py35_coro():
    s = await stuff()
    return s


async def main():
    print("beg")
    # r = py34_coro()         # <generator object py34_coro at 0x7fbe12da4ba0>
    # r = await asyncio.gather(py34_coro())
    r = await asyncio.gather(py35_coro())
    print(r)
    print("end")


if __name__ == '__main__':
    asyncio.run(main())