# 01. Create a CSV sample dataset
import random
import csv
from faker import Faker

# Initialize Faker
fake = Faker()

# List of products and their categories
products = [
    {"name": "Laptop", "category": "Electronics", "price": 899.99},
    {"name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"name": "Headphones", "category": "Accessories", "price": 49.99},
    {"name": "Coffee Maker", "category": "Home Appliances", "price": 79.99},
    {"name": "Sneakers", "category": "Fashion", "price": 59.99},
    {"name": "Backpack", "category": "Fashion", "price": 39.99},
    {"name": "Blender", "category": "Home Appliances", "price": 99.99},
    {"name": "Desk Chair", "category": "Furniture", "price": 129.99},
    {"name": "Water Bottle", "category": "Accessories", "price": 19.99},
    {"name": "Notebook", "category": "Stationery", "price": 5.99},
]

# Define a function to generate order data
def generate_order_data(num_rows):
    data = []
    for _ in range(num_rows):
        product = random.choice(products)
        quantity = random.randint(1, 10)
        total = round(product["price"] * quantity, 2)
        order = {
            "Order ID": fake.uuid4(),
            "Customer Name": fake.name(),
            "Customer Email": fake.email(),
            "Product Name": product["name"],
            "Category": product["category"],
            "Quantity": quantity,
            "Price": product["price"],
            "Total": total,
            "Order Date": fake.date_this_year(),
            "Shipping Address": fake.address(),
        }
        data.append(order)
    return data

# Generate 1000 rows of data
num_rows = 1000
order_data = generate_order_data(num_rows)

# Save the data to a CSV file
output_file = "sample_orders.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=order_data[0].keys())
    writer.writeheader()
    writer.writerows(order_data)

print(f"Sample dataset with {num_rows} rows has been saved to '{output_file}'.")
