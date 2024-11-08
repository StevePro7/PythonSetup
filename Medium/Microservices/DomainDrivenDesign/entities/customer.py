# entities/customer.py
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def update_email(self, new_email):
        self.email = new_email

# Usage
customer = Customer(customer_id=1, name="John Doe", email="john.doe@example.com")
print(customer.name)  # Output: John Doe
customer.update_email("john.new@example.com")
print(customer.email)  # Output: john.new@example.com