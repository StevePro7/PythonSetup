class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Fish:
    def swim(self):
        return "I am swimming!"

def make_animal_speak(animal):
    # We don't care about the type just that the object has a 'speak' method
    speak = animal.speak()
    print(speak)


dog = Dog()
cat = Cat()
fish=Fish()

make_animal_speak(dog)      # Output: Woof!
make_animal_speak(cat)      # Output: Meow!
make_animal_speak(fish)     # AttributeError: 'Fish' object has no attribute 'speak'