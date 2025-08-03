# Pattern 2: Exception Handling in Concurrent Operations
import asyncio

async def might_fail(task_id):
    await asyncio.sleep(0.5)
    if task_id == 2:
        raise ValueError(f"Task {task_id} failed")
    return f"Task {task_id} succeeded"

async def handle_partial_failures():
    """"""
    tasks = [might_fail(i) for i in range(5)]

    # gather with return_exceptions=True
    results = await asyncio.gather(*tasks, return_exceptions=True)

    successes = []
    failures = []

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failures.append(f"Task {i}: {result}")
        else:
            successes.append(result)

    print(f"Successes: {successes}")
    print(f"Failures: {failures}")

asyncio.run(handle_partial_failures())
