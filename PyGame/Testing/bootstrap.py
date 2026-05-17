from ServiceRegistry import ServiceRegistry
from Managers.BarManager import BarManager
from Managers.FooManager import FooManager

def build_game():
    ServiceRegistry.register(FooManager.__name__, FooManager())
    ServiceRegistry.register(BarManager.__name__, BarManager())

    return True