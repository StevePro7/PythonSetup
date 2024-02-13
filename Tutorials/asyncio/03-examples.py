import asyncio


async def z(x):
    return x


async def f(x):
    y = await z(x)
    return y


async def g(x):
    yield x


#async def m(x):
#    yield from gen(x)       # SyntaxError: 'yield from' inside async function


#def m(x):
#    y = await z(x)          # SyntaxError: 'await' outside async function
#    return y


async def main():
    print("beg")
    y = await f(1)
    # y = g(2)                # <async_generator object g at 0x7f3ac2fe3670>
    # y = await m(3)
    print(y)
    print("end")


if __name__ == '__main__':
    asyncio.run(main())