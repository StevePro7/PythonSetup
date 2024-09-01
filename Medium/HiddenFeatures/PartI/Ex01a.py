def add_subject(name, subject, subjects=[]) -> list:
    subjects.append(subject)
    return {'name': name, 'subjects': subjects}

print(add_subject('person1', 'subject1'))
print(add_subject('person2', 'subject2'))
print(add_subject('person3', 'subject3'))

# OUTPUT
# {'name': 'person1', 'subjects': ['subject1']}
# {'name': 'person2', 'subjects': ['subject1', 'subject2']}
# {'name': 'person3', 'subjects': ['subject1', 'subject2', 'subject3']}
