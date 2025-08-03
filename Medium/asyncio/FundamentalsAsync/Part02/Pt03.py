# Pattern 3: Retry Mechanisms
import asyncio
import random


async def unreliable_api_call():
    """"""
    if random.random() < 0.7:           # 70% failure rate
        raise ConnectionError("API unavailable")
    return "API success"

async def retry_with_backoff(max_retires=3):
    """"""
    for attempt in range(max_retires):
        try:
            result = await unreliable_api_call()
            print(f"Success on attempt {attempt + 1}")
            return result
        except ConnectionError as e:
            if attempt == max_retires - 1:
                print(f"Failed after {max_retires} attempts")
                raise

            wait_time = 2 ** attempt
            print(f"Attempt {attempt + 1} failed, retrying in {wait_time}")
            await asyncio.sleep(wait_time)


asyncio.run(retry_with_backoff())
