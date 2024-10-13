import pickle


# Define a class with properties and methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def to_upper(self):
    return self.name.upper()

# Class instance
data = Person("John", 36)

# Open a file in binary write mode
with open("data.pkl", "wb") as file:
    # Serialize the class instance and write it to the file
    pickle.dump(data, file)

print("Data has been pickled.")