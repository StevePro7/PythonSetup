# 5. Filter Function
def filter_high_sales(sales, threshold):
    return list(filter(lambda x: x > threshold, sales))

print(filter_high_sales([100, 200, 50, 300, 150], 150))
