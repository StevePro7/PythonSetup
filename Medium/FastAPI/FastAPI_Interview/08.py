# 8. Error Handling
from fastapi import FastAPI, HTTPException
from http import HTTPStatus

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id > 10:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")
    return {"item_id": item_id}
