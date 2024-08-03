from fastapi import FastAPI
from contextlib import asynccontextmanager

# from routers.api import router # add this later
from utils.init_db import create_tables

# @app.on_event("startup")
# def on_startup() -> None:
#     """
#     Initializes the database tables when the application starts up.
#     """
#     create_tables()
# # app.include_router(router)



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Application startup")
    create_tables()
    yield
    # Shutdown event
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)
#app = FastAPI(debug=True, title="Tutorial")
@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)