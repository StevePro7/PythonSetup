from ship04.shipcon import ShippingContainer
import iso6346

class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)

        # Assign via property and get validation for free
        self._celsius = celsius


    @property
    def celsius(self):
        return self._celsius


    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self._celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

