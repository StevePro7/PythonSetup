from fastapi import FastAPI
from utils.init_db import create_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Application startup")
    create_tables()
    yield
    print("Application shutdown")


#app = FastAPI(debug=True, title="Tutorial")
app = FastAPI(debug=True, title="Tutorial", lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)