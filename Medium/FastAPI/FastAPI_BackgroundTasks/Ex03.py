from fastapi import FastAPI, Request, BackgroundTasks

app = FastAPI()


async def custom_background_function():
    pass

@app.middleware("http")
async def add_background_task_middleware(request: Request, call_next):
    background_tasks = BackgroundTasks()
    background_tasks.add_task(custom_background_function)
    response = await call_next(request)
    response.background = background_tasks
    return response
