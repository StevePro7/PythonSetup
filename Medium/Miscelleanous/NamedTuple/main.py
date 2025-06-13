from collections import namedtuple

User = namedtuple('User', ['id', 'name', 'age'])

u1 = User(id=1, name='stevepro', age=24)

print(u1.name)
print(u1[2])



Car = namedtuple('Car', ['brand', 'model', 'year'])
my_car = Car('Toyota', 'Corolla', 2004)
print(Car._fields)

print(my_car._asdict())


new_car = my_car._replace(year=2012)
print(new_car)


Car2 = namedtuple('Car', ['brand', 'model', 'year'], defaults=['Unknown', 'Unknown', 2020])
car2 = Car2()
print(car2)
