from ship06.shipref import RefrigeratedShippingContainer


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super(HeatedRefrigeratedShippingContainer, self)._set_celsius(value)

