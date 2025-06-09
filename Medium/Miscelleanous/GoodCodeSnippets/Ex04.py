class Bird:
    def speak(self):
        return "Chirp!"

class Duck(Bird):
    def speak(self):
        return "Quack!"

# common superclass
def animal_sound(animal):
    print(animal.speak())

bird = Bird()
duck = Duck()

animal_sound(bird)  # Output: Chirp!
animal_sound(duck)  # Output: Quack!