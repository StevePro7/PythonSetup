from file_controller import FileController
from user_controller import UserController

file_controller: FileController = FileController()
user_controller: UserController = UserController(file_controller)

file: str = "user.yaml"
user_controller.open_file(file)
user_controller.deserialize()
user_controller.report()