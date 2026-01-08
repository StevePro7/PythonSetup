from file_controller import FileController
from user import User, UserSchema

class UserController:
    def __init__(self, file_controller: FileController):
        self.file_controller = file_controller

    def open_file(self, file: str):
        self.data: dict = self.file_controller.open_file(file)

    def deserialize(self):
        self.user: User = UserSchema.load(self.data)

    def report(self):
        print(self.user.name)
        print(self.user.email)