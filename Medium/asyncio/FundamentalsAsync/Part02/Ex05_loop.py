import asyncio

def create_custom_loop():
    """Create custom event loop with specific configuration"""
    loop = asyncio.new_event_loop()

    # Configure the loop
    loop.set_debug(True)        # Enable debug mode

    # Set custom exception handler
    def exception_handler(loop, context):
        print(f"Custom exception handler: {context['message']}")
        if 'exception' in context:
            print(f"Exception: {context['exception']}")

    loop.set_exception_handler(exception_handler)
    return loop

async def custom_loop_demo():
    print("Running with custom event loop")
    await asyncio.sleep(0.1)
    # Create a coroutine and neven wait it to trigger debug warning
    async def never_awaited():
        await asyncio.sleep(1)
    never_awaited()         # Not awaited on purpose


# Using custom loop
custom_loop = create_custom_loop()
asyncio.set_event_loop(custom_loop)

try:
    custom_loop.run_until_complete(custom_loop_demo())
finally:
    custom_loop.close()