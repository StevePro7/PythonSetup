from ship00 import shipcon

if __name__ == '__main__':
    sc = shipcon.ShippingContainer("oc", "ct")
    nn = sc._get_next_serial()
    print(nn)
    print(sc.owner_code)