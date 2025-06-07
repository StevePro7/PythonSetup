from ship01 import shipcon

if __name__ == '__main__':
    sc = shipcon.ShippingContainer("oc", "ct")
    nn = sc._get_next_serial()
    print(nn)
    print(sc.owner_code)

    sc2 = sc.create_empty("oc2")
    print(sc2.owner_code)

    sc3 = sc.create_with_items("oc3", (1,2,3,4))
    print(sc3.owner_code)
    print(sc3.contents)
