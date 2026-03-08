Async ≠ Concurrent: Why 90% of Python Developers Get Concurrency Wrong
08-Mar-2026

https://python.plainenglish.io/async-concurrent-why-90-of-python-developers-get-concurrency-wrong-0a79dfae362e


mkdir -p ~\GitHub\StevePro9\PythonSetup\Medium\asyncio\AsyncNotConcurrency
uv init --python 3.11
uv venv --python 3.11
.venv\Scripts\activate


async / await
don't give you concurrency immediately - only ability to pause and resume

to actually run things concurrently you need to schedule multiple tasks
at the same time
e.g.

asyncio
create_task()
gather()
TaskGroup


Coroutine
special Python function that can pause and resume

- define coroutine async def
- pause coroutine with await
- event loop decides when to resume coroutine


Ex01
# <coroutine object greet at 0x0000029463340700>

to run coroutine you must give it to the event loop
asyncio.run(greet())


Ex02
Common misconception
await fd()
await fd()
await fd()

sequential processing
because await blocks until the current coroutine finishes

here code is asynchronous BUT NOT concurrent
# Total time: 6.04s


Ex03
Fix: schedule with create_task()

to run independent tasks together you MUST schedule them
now all tasks overlap - program time = slowest task time
# Total time: 2.01s


Mental Model: Async != Concurrent
- async = lets you define coroutine [pause / resume]
- await = tells coroutine to pause until something finishes
- create_task() = puts multiple coroutines into event loop [at same time]


Alternatives to create_task()

- asyncio.gather()
results = await asyncio.gather(
    fetch_data("https://api1.com"),
    fetch_data("https://api2.com"),
    fetch_data("https://api3.com"),
)

- asyncio.as_completed()
for task in asyncio.as_completed([
    fetch_data("https://api1.com"),
    fetch_data("https://api2.com"),
    fetch_data("https://api3.com"),
]):
    result = await task
    print("Got:", result)

- TaskGroup
async with asyncio.TaskGroup() as tg:
    tg.create_task(fetch_data("https://api1.com"))
    tg.create_task(fetch_data("https://api2.com"))
    tg.create_task(fetch_data("https://api3.com"))


Ex04
Real-World example: API Rate limit


Common Pitfalls

- BAD sequential awaits
res1 = await op1()
res2 = await op2()

- GOOD concurrent scheduling
res1, res2 = await asyncio.gather(op1(), op2())


- BAD creating tasks too late
t1 = asyncio.create_task(op1())
res1 = await t1   # already waited before creating the next

- GOOD create all tasks first then await
t1 = asyncio.create_task(op1())
t2 = asyncio.create_task(op2())
res1, res2 = await asyncio.gather(t1, t2)


IMPORTANT
Sequential: when tasks depend on each other
user = await fetch_user()
settings = await fetch_settings(user.id)

Concurrent: when tasks are independent and I/O-bound
user_task = asyncio.create_task(fetch_user())
settings_task = asyncio.create_task(fetch_settings())
user, settings = await asyncio.gather(user_task, settings_task)


SUMMARY
- Coroutines = functions that can pause and resume
- async / await != concurrency by itself
- await waits while create_task() schedules
- use gather() or TaskGroup to combine tasks
- control concurrency with semaphores
- CPU-heavy work use threads or processes NOT async


Finally once you use create_task() [or TaskGroup] async code becomes truly concurrent