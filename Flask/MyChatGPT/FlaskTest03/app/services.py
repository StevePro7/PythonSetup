from app.models import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, name, email):
        user = User(name=name, email=email)
        return self.user_repository.create(user)

    def delete_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.user_repository.delete(user)
            return True
        return False
