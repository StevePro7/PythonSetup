class Meta(type):
    def __new__(cls, *args, **kwargs):
        print(f"Creating class")
        return super().__new__(cls, args, kwargs)


class MyClass(metaclass=Meta):
    pass