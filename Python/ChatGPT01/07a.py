class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Fish:
    pass


def make_animal_speak(animal):
    animal.speak()


dog = Dog()
cat = Cat()
fish = Fish()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(fish) # Output: Fish cannot speak!