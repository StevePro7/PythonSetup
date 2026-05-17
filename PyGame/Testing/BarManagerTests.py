from ServiceRegistry import ServiceRegistry
from FooManager import FooManager
from BarManager import BarManager
from bootstrap import build_game

build_game()
# ServiceRegistry.register(FooManager.__name__, FooManager())
# ServiceRegistry.register(BarManager.__name__, BarManager())

bar = ServiceRegistry.get(BarManager.__name__)
bar.LoadContent()