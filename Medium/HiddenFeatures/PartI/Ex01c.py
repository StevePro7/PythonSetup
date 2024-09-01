def add_subject(name, subject: str, subjects: list=None) -> list:
    if subjects is None:
        subjects = []

    subjects.append(name)
    return {'name': name, 'subjects': subjects}


print(add_subject.__defaults__)
print(add_subject('person1', 'subject1'))
print(add_subject('person2', 'subject1'))
print(add_subject('person3', 'subject1'))


# OUTPUT
# (None,)
# {'name': 'person1', 'subjects': ['person1']}
# {'name': 'person2', 'subjects': ['person2']}
# {'name': 'person3', 'subjects': ['person3']}