from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a path operation (route) for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)