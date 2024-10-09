class InchToCmDescriptor:
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Height must be a number.")
        instance._inches = value / 2.54

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._inches * 2.54

    def __delete__(self, instance):
        del instance._inches


class Height:
    height_cm = InchToCmDescriptor()

    def __init__(self, inches) -> None:
        self._inches = inches


height: Height = Height(70)
result: float = height.height_cm
print(result)

height.height_cm = 180
result = height._inches
print(height._inches)