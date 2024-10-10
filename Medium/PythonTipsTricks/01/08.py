from collections import namedtuple

Student = namedtuple("Student", "name, age, grade")

lines = [
   ["Albie Bailey", 21, 3],
   ["Brooklyn Price", 23, 5],
   ["Noah Hawkins", 19, 1],
   ["Marcel Hall", 25, 6],
   ["Dominik Davis", 20, 1],
   ["Clayton Elliott", 21, 3],
]

students = list(map(Student._make, lines))
print(students)
