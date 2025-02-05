def countdown(n: int):
    while n > 0:
        yield n         # Pause and return n
        n -= 1


# Create the generator
gen = countdown(5)


# Iterating over the generator
for num in gen:
    print(num)
