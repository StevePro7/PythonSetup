import asyncio

async def async_operation(future, data):
    await asyncio.sleep(1)

    if data == "success":
        future.set_result("Op succeed")
    else:
        future.set_exception(RuntimeError("Op failed"))


def future_callback(future):
    try:
        print("Callback:", future.result())
    except Exception as exc:
        print("Callback:", exc)


async def main():
    future = asyncio.Future()

    future.add_done_callback(future_callback)

    await async_operation(future, "success")

    if future.done():
        try:
            print("Main:", future.result())
        except Exception as exc:
            print("Main:", exc)


asyncio.run(main())