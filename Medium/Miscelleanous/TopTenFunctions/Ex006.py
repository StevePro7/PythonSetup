# 6. Sorted Function
def sort_sales_data_by_sales(data):
 return sorted(data, key=lambda x: x['Sales'])
sales_data = [
 {'Product': 'Laptop', 'Sales': 150},
 {'Product': 'Mouse', 'Sales': 300},
 {'Product': 'Keyboard', 'Sales': 200},
]

print(sort_sales_data_by_sales(sales_data))