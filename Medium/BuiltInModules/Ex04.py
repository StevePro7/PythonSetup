import random

print(random.randint(1, 10))

my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list))

print(random.random())

my_sequence = ["apple", "banana", "orange", "grape"]
print(random.choice(my_sequence))

print(random.sample(range(1, 101), 5))

random_element_with_replacement = random.choices(["A", "B", "C", "D"], k=3)  # Select 3 elements with replacement
print("Random Element with Replacement:", random_element_with_replacement)

random.seed(1234)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

random.seed(1234)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))