# 7. Enumerate Function
def list_products_with_index(products):
 for index, product in enumerate(products):
  print(f"{index + 1}. {product}")

list_products_with_index(['Laptop', 'Mouse', 'Keyboard'])