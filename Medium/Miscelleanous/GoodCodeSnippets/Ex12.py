class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute {name} not found"

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = DynamicAttributes()
obj.x = 10  # Output: Setting x to 10
print(obj.x)  # Output: 10
print(obj.y)  # Output: Attribute y not found