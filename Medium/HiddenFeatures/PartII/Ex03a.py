class ObjectDef:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    # def set_x(self, x):
    #     self._x = x

def print_values():
    obj = ObjectDef(0)
    obj.set_x(42)
    print(obj.get_x())


print_values()