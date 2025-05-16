from abc import ABC, abstractmethod
from typing import List, Optional
from models.schemas.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass