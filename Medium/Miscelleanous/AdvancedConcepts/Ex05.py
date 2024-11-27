class Decorator:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value * 2


class MyClass:
    attribute = Decorator()


obj = MyClass()
obj.attribute = 10
print(obj.attribute)        # 20