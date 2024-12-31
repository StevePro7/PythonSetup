# 07. Manage Context (with Blocks)
class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Resource released '{exc_type}', '{exc_val}', '{exc_tb}'")

with ManagedResource():
    print("Using an resource")