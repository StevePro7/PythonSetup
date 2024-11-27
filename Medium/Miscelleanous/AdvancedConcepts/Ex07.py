class Bird:
    def fly(self):
        print("Flying")


class Airplane:
    def fly(self):
        print("Flying with engines")


def test_fly(obj):
    obj.fly()


test_fly(Bird())
test_fly(Airplane())