from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.api import router
from utils.init_db import create_tables

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Application startup")
    create_tables()
    yield
    print("Application shutdown")


origins = ["*"]
#app = FastAPI(debug=True, title="Tutorial")
app = FastAPI(debug=True, title="Tutorial", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
