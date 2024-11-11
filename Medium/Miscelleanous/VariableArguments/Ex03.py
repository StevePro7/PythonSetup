def display_details(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_details(1, 2, 3, name="Charlie", age=25, hobby="Coding")
