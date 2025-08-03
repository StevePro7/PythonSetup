# Pattern 1: Timeout Patterns
import asyncio

async def unreliable_operation():
    """"""
    await asyncio.sleep(3)
    return "Success"

async def with_timeout():
    try:
        result = await asyncio.wait_for(unreliable_operation(), timeout=2.0)
        return result
    except asyncio.TimeoutError:
        print("Operation timed out")
        return "Timeout fallback"

async def multiple_timeouts():
    """"""
    async def safe_operation(op_id):
        try:
            await asyncio.sleep(op_id)
            return f"Operation {op_id} succeeded"
        except asyncio.CancelledError:
            return f"Operation {op_id} was cancelled"

    # Wrap coroutines in tasks we can cancel/check them
    tasks = [asyncio.create_task(safe_operation(i)) for i in [0.5, 3, 1]]

    try:
        # All operations must complete within 2 seconds
        results = await asyncio.wait_for(
            asyncio.gather(*tasks),
            timeout=2.0
        )
        return results
    except asyncio.TimeoutError:
        print("Some ops timed out")
        # Cancel remaining tasks
        for task in tasks:
            if not task.done():
                task.cancel()
        # Optionall gather results completed / cancelled tasks
        results = []
        for task in tasks:
            try:
                results.append(await task)
            except asyncio.CancelledError:
                results.append("Cancelled")
        return results

#print(asyncio.run(with_timeout()))
print(asyncio.run(multiple_timeouts()))