from repositories import UserRepository
from serializers import UserSchema

class UserService:
    def __init__(self, user_repository: UserRepository, user_schema: UserSchema):
        self.user_repository = user_repository
        self.user_schema = user_schema

    def get_user_by_id(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        return self.user_schema.dump(user)

    def get_all_users(self):
        users = self.user_repository.get_all_users()
        return self.user_schema.dump(users, many=True)

    def create_user(self, name: str, email: str):
        user = self.user_repository.create_user(name, email)
        return self.user_schema.dump(user)
