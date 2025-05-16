from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_models.product_db import Base
from repositories.product_repository import ProductRepository
from repositories.sql_alchemy_product_repository import SqlAlchemyProductRepository
def get_sqlalchemy_repository() -> ProductRepository:
    engine = create_engine("sqlite:///products.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return SqlAlchemyProductRepository(Session())