# 6. Automatic Interactive Documentation
from fastapi import FastAPI


app = FastAPI(
    title="Custom API",
    description="This is a custom description for the API.",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Custom API documentation!"}
