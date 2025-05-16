from fastapi import Depends, FastAPI, HTTPException
from dependencies import get_sqlalchemy_repository
from models.schemas.product import Product
from services.product_service import ProductService
import http
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World!"


@app.get("/products")
def list_products(
        repo=Depends(get_sqlalchemy_repository)
):
    service = ProductService(repo)
    return service.list_products()


@app.get("/products/{product_id}")
def read_product(
        product_id: int,
        repo=Depends(get_sqlalchemy_repository)
):
    service = ProductService(repo)
    product = service.get_product(product_id)
    if not product:
        detail = f"Product [{product_id}] not found"
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=detail)
    return product.dict()


@app.post("/products")
def create_product(
        name: str,
        price: float,
        repo=Depends(get_sqlalchemy_repository)
):
    service = ProductService(repo)
    product = service.create_product(name, price)
    return product.dict()


@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    name: str,
    price: float,
    repo = Depends(get_sqlalchemy_repository)
):
    service = ProductService(repo)
    updated_product = service.update_product(product_id, name, price)
    if not updated_product:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Product not found")
    return updated_product.dict()


@app.delete("/products/{product_id}")
def delete_product(
        product_id: int,
        repo=Depends(get_sqlalchemy_repository)
):
    service = ProductService(repo)
    success = service.delete_product(product_id)
    if not success:
        detail = f"Product [{product_id}] not found"
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail=detail)
    message = f"Product [{product_id}] deleted successfully"
    return {"message": message}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

