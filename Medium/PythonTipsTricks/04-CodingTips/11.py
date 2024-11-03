# 11. Use sorted() with custom keys: flexible sorting
students = [
    {'name': 'John', 'grade': 90},
    {'name': 'Jane', 'grade': 85},
    {'name': 'Dave', 'grade': 92}
]

def get_grade(student):
    return student['grade']

students.sort(key=get_grade)
print(students)
print()

# Condensed way: using sorted() with lambda function
sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)