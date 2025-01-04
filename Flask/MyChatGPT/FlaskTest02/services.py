from repositories import UserRepository
from pydantic_models import UserCreateRequest, UserResponse

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repository.get_user_by_id(user_id)
        return UserResponse.from_orm(user)

    def get_all_users(self) -> list[UserResponse]:
        users = self.user_repository.get_all_users()
        return [UserResponse.from_orm(user) for user in users]

    def create_user(self, user_data: UserCreateRequest) -> UserResponse:
        user = self.user_repository.create_user(user_data.name, user_data.email)
        return UserResponse.from_orm(user)
