class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class AuthenticateMixin:
    def authenticate(self, user):
        print(f"Authenticating user: {user}")


class UserService(LoggingMixin, AuthenticateMixin):
    def create_user(self, username):
        self.log(f"Creating user: {username}")
        self.authenticate(username)
        print(f"User {username} created.")


# Using the class
user_service = UserService()
user_service.create_user("Alice")