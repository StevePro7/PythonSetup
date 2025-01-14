# 2. Help Function
def calculate_discounted_price(price, discount):
    """ Calculate the discounted price of a product.

    price: original price of the product
    discount: discount percentage to be applied returns: float
    """

    return price * (1 - discount / 100)


help(calculate_discounted_price)
