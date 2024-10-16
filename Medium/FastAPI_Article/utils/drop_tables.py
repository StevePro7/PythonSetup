from config.database import Base, engine
from models.region import Region
from models.city import City


def drop_tables():
    """
    Drops all database tables defined in the application.
    """
    Base.metadata.drop_all(bind=engine)
    Region.metadata.drop_all(bind=engine)
    City.metadata.drop_all(bind=engine)
