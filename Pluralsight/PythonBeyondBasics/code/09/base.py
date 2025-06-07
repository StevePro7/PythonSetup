class Base:
    def __init__(self):
        print('Base init')

    def f(self):
        print('Base f()')


class Sub(Base):
    def __init__(self):
        super(Sub, self).__init__()
        print('Sub init')

    def f(self):
        print('Sub f()')