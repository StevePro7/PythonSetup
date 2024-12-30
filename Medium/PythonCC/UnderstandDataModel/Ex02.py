# 02. Attribute Access
class AttributeHandler:
    def __init__(self):
        self.attributes = {}

    def __getattr__(self, item):
        return self.attributes.get(item, f"{item} not found")

    def __setattr__(self, key, value):
        if key == "attributes":
            super().__setattr__(key, value)
        else:
            self.attributes[key] = value

obj = AttributeHandler()
obj.color = "blue"
print(obj.color)
print(obj.size)