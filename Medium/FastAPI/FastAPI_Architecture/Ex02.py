class BaseService:
    def __init__(self):
        #self.db = get_database()
        #self.logger = get_logger()
        #self.cache = get_cache()
        pass


class UserService(BaseService):
    async def create(self, user):
        self.logger.info("Creating user")
        return await self.db.users.insert_one(user.dict())


class OrderService(BaseService):
    async def create(self, user):
        self.logger.info("Creating oder")
        return await self.db.orders.insert_one(user.dict())
