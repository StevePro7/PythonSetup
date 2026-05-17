from ServiceRegistry import ServiceRegistry
from FooManager import FooManager
from BarManager import BarManager

def build_game():
    ServiceRegistry.register(FooManager.__name__, FooManager())
    ServiceRegistry.register(BarManager.__name__, BarManager())

    return True