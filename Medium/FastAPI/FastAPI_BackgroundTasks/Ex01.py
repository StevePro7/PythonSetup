from fastapi import FastAPI, BackgroundTasks
from datetime import datetime

app = FastAPI()


def log_message(message: str):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()}: {message}\n")


@app.post("/send-message")
async def send_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_message, message)
    return {"message": "Message received.  It will logged shortly."}
