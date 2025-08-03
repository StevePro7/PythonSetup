# Pattern 2: Async Context Management
import asyncio

class AsyncResource:
    """
    """
    async def __aenter__(self):
        print("Resource acquiring")
        await asyncio.sleep(0.1)
        print("Resource acquired")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Resource releasing")
        await asyncio.sleep(0.1)
        print("Resource released")

    async def do_work(self):
        print("doing work")
        await asyncio.sleep(0.5)
        return "Work complete"



async def use_resource():
    async with AsyncResource() as resource:
        result = await resource.do_work()
        return result


asyncio.run(use_resource())