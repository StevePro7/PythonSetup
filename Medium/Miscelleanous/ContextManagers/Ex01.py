class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Can return a resource or helper object

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_type.__name__}")
        # Returning False re-raises exceptions; True suppresses them
        return False

with MyContextManager() as manager:
    print("Inside the block")
    # Uncomment the next line to see exception handling in action:
    # raise ValueError("Oops!")


# OUTPUT
# Entering the context
# Inside the block
# Exiting the context