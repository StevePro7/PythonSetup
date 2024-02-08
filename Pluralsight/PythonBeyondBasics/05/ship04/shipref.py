from ship04.shipcon import ShippingContainer
import iso6346

class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))


    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
            return ValueError("Temp too hot!")

        self._celsius = celsius


    @property
    def celsius(self):
        return self._celsius


    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self._celsius = value

