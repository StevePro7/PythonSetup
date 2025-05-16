from typing import List, Optional

from models.schemas.product import Product
from repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, name: str, price: float) -> Product:
        product = Product(name=name, price=price)
        self.repository.add(product)
        return product

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.repository.get_by_id(product_id)

    def list_products(self) -> List[Product]:
        return self.repository.list_all()

    def update_product(self, product_id: int, name: str, price: float) -> Optional[Product]:
        product = self.repository.get_by_id(product_id)
        if product:
            updated_product = Product(id=product_id, name=name, price=price)
            self.repository.update(updated_product)
            return updated_product
        return None

    def delete_product(self, product_id: int) -> bool:
        product = self.repository.get_by_id(product_id)
        if product:
            self.repository.delete(product_id)
        return product is not None