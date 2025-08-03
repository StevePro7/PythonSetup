import asyncio

async def might_fail(task_id):
    await asyncio.sleep(1)
    if task_id == 2:
        raise ValueError(f"Task {task_id} failed!")
    return f"Task {task_id} succeeded"

async def handle_simple_errors():
    try:
        result = await might_fail(2)
        print(result)
    except ValueError as e:
        print(f"Caught {e}")

asyncio.run(handle_simple_errors())
