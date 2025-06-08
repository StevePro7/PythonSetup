class Descriptor:
    def __get__(self, instance, owner):
        return f"Getting attribute from {owner}"

    def __set__(self, instance, value):
        print(f"Setting attribute to {value}")

    def __delete__(self, instance):
        print("Deleting attribute")

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 10  # Output: Setting attribute to 10
print(obj.attr)  # Output: Getting attribute from <class '__main__.MyClass'>
del obj.attr  # Output: Deleting attribute