# 05. Object Creation and Destruction
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Resource {self.name} created")

    def __del__(self):
        print(f"Resource {self.name} destoryed")

r = Resource("FileHandler")