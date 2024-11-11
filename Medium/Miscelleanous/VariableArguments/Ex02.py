def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Wonderland")
print()
print_info(name="Bob", occupation="Builder")
