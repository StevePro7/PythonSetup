class ObjectDef:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

def print_values():
    obj = ObjectDef(0)
    obj.x = 42
    print(obj.x)


print_values()