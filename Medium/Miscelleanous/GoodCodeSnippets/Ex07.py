class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

class Vehicle(LoggingMixin):
    def __init__(self, name):
        self.name = name

    def start(self):
        self.log(f"{self.name} started")
        return "Vroom!"

car = Vehicle("Tesla")
print(car.start())  # Output: Log: Tesla started \n Vroom!