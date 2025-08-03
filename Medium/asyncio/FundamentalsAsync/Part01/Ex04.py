import asyncio

async def task_one():
    print("T1 BEG")
    await asyncio.sleep(2)
    print("T1 end")
    return "T1"

async def task_two():
    print("T2 BEG")
    await asyncio.sleep(1)
    print("T2 end")
    return "T2"

async def run_sequential():
    print("SEQ beg")
    result1 = await task_one()
    result2 = await task_two()
    print("SEQ end")
    return [result1, result2]


async def run_concurrent():
    print("CON beg")
    results = await asyncio.gather(
        task_one(),
        task_two()
    )
    print("CON end")
    return results

print("seq")
asyncio.run(run_sequential())

print("con")
asyncio.run(run_concurrent())
