from models import db, User
from sqlalchemy.orm import sessionmaker

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user_by_id(self, user_id: int) -> User:
        return self.db_session.query(User).get(user_id)

    def get_all_users(self) -> list:
        return self.db_session.query(User).all()

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.db_session.add(user)
        self.db_session.commit()
        return user
