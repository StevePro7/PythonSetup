# 01.
int_num = 42
float_num = 3.14
string_var = "Hello, Python!"
bool_var = True


# 02.
x = 10
y = "Python"


# 03.
my_list = [1, 2, 3, "Python"]
my_tuple = (1, 2, 3, "Tuple")


# 04.
my_dict = {'name': 'John', 'age': 25, 'city': 'Pythonville'}


# 05.
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
for item in my_list:
    print(item)
while True:
    # code


# 06.
def greet(name="User"):
    return f"Hello, {name}!"
result = greet("John")


# 07.
class Dog:
    def __init__(self, name):
        self.name = name
def bark(self):
        print("Woof!")
my_dog = Dog("Buddy")
my_dog.bark()


# 08.
with open("file.txt", "r") as file:
    content = file.read()
with open("new_file.txt", "w") as new_file:
    new_file.write("Hello, Python!")


# 09.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")


# 10.
import math
from datetime import datetime
result = math.sqrt(25)
current_time = datetime.now()


