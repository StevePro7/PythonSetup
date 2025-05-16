from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

    class Config:
        #orm_mode = True
        #allow_population_by_field_name = True
        from_attributes = True
        validate_by_name = True