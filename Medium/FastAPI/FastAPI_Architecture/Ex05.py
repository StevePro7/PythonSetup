class MongoClient:
    pass


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(
#                settings.database_url,
#                maxPoolSize=50
            )
        return cls._instance


db = Database()


class UserService:
    def __init__(self):
        self.db = db


class OrderService:
    def __init__(self):
        self.db = db
