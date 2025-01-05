from app.models import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def create(self, user):
        self.db_session.add(user)
        self.db_session.commit()
        return user

    def delete(self, user):
        self.db_session.delete(user)
        self.db_session.commit()
