# 9. Open Function
def write_sales_to_file(filename, content):
 """Writes content into file"""
 with open(filename, "w") as file:
  file.write(content)


def read_sales_file(filename):
 """Reads content in file only"""
 with open(filename, "r") as file:
  return file.read()


def append_sales_to_file(filename, content):
 """Appends new content to original content"""
 with open(filename, "a") as file:
  file.write(content)

write_sales_to_file("sales.txt", "Product: Laptop\nSales: 150")
print(read_sales_file("sales.txt"))

append_sales_to_file("sales.txt", "\nProduct: Mouse\nSales: 300")
print(read_sales_file("sales.txt"))