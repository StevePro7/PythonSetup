import pickle


# Define a class with properties and methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def to_upper(self):
    return self.name.upper()


# Open the file in binary read mode
with open("data.pkl", "rb") as file:
    # Deserialize the data
    loaded_data = pickle.load(file)

print("Unpickled Data:", loaded_data)

# Read properties and call methods from unpickled class instance
print(loaded_data.name)
print(loaded_data.age)
print(loaded_data.to_upper())