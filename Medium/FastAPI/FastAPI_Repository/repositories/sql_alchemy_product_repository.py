from typing import List, Optional
from sqlalchemy.orm import Session
from models.db_models.product_db import ProductDB
from models.schemas.product import Product
from repositories.product_repository import ProductRepository


class SqlAlchemyProductRepository(ProductRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, product_id: int) -> Optional[Product]:
        product_db = self.session.query(ProductDB).get(product_id)
        if product_db:
            return Product(
                id=product_db.id,
                name=product_db.name,
                price=product_db.price
            )
        return None

    def add(self, product: Product) -> None:
        product_dict = product.dict()
        product_db = ProductDB(**product_dict)
        self.session.add(product_db)
        self.session.commit()

    def list_all(self) -> List[Product]:
        product_db = self.session.query(ProductDB).all()
        return [Product.from_orm(p) for p in product_db]

    def update(self, product: Product) -> None:
        product_db = self.session.query(ProductDB).get(product.id)
        if product_db:
            product_db.name = product.name
            product_db.price = product.price
            self.session.commit()

    def delete(self, product_id: int) -> None:
        product_db = self.session.query(ProductDB).get(product_id)
        if product_db:
            self.session.delete(product_db)
            self.session.commit()