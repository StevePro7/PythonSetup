import asyncio
import asyncpg
from fastapi import FastAPI

app = FastAPI()

# Async function that fetches data from a database
async def _fetch_db_data():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='dbname',
        host='localhost'
    )
    rows = await conn.fetch("SELECT * FROM your_table WHERE some_column = 'some_value'")
    await conn.close()
    return rows

# FastAPI endpoint that calls the inner function for database query
@app.get("/call_other_service")
async def call_other_service():
    data = await _fetch_db_data()
    return {"data": data}

# Synchronous function for CPU-intensive computation
def _factorize():
    # CPU-intensive computation
    ...

@app.get("/factorize")
async def factorize():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _factorize)
    return result

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
