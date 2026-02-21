from my_api_py import Guitar

def pprint_axe(guitar: Guitar) -> None:
    print(f"Guitar: '{guitar.manufacturer}' [{guitar.num_strings}-string] = ${guitar.price}")

print("beg")

guitar1 = Guitar("Fender", 1500.0, 6)
guitar2 = Guitar("Ibanez", 1200.0)
guitar2.num_strings = 7

guitar3 = Guitar()
guitar3.set_manufacturer("Gibson")
guitar3.set_price(2400)
guitar3.num_strings = 6
#guitar3.price = 100.0          # AttributeError: property of 'Guitar' object has no setter
#guitar3.manufacturer = "Foo"    # AttributeError: property of 'Guitar' object has no setter

pprint_axe(guitar1)
pprint_axe(guitar2)
pprint_axe(guitar3)

print("end")