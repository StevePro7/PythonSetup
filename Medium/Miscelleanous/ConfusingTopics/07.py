class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("I'm a dog, but I can quack!")


def make_it_quack(duck):
    duck.quack()


make_it_quack(Dog())