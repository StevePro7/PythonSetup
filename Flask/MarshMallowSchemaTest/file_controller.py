import yaml

class FileController:
    def open_file(self, file: str) -> dict:
        with open(file, "r") as f:
            data: dict = yaml.safe_load(f)
            return data
