# 9. Class Methods and Static Methods
class Enchanter:
    @staticmethod
    def enchant(item):
        print(f"{item} is enchanted!")
    @classmethod
    def summon(cls):
        print("A new enchanter is summoned.")


# 10. Properties and Setters
class Elementalist:
    def __init__(self, element):
        self._element = element
    @property
    def element(self):
        return self._element
   @element.setter
    def element(self, value):
        if value in ["Fire", "Water", "Earth", "Air"]:
            self._element = value
        else:
            print("Invalid element!")