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
    if hasattr(animal, 'speak') and callable(animal.speak):
        speak = animal.speak()
        print(speak)
    else:
        raise TypeError("Object does not implement the 'speak' method!")


dog = Dog()
cat = Cat()
fish=Fish()

make_animal_speak(dog)      # Output: Woof!
make_animal_speak(cat)      # Output: Meow!
make_animal_speak(fish)     # AttributeError: 'Fish' object has no attribute 'speak'