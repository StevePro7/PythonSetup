from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/items/{item_id}")
@limiter.limit("5/minute")
async def read_item(item_id: int):
    return {"item_id": item_id}