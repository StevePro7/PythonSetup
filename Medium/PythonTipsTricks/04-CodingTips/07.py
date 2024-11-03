# 07. Generators: efficient memory usage
numbers = [x ** x for x in range(1000000)]
# Process numbers here


# Condensed way: using Generators
numbers2 = (x ** 2 for x in range(1000000))
# Process numbers here

# IMPORTANT
# notice [] replaced by ()
# () version generates values as needed keeping memory usage low