from ServiceRegistry import ServiceRegistry
from Managers.BarManager import BarManager
from bootstrap import build_game

build_game()

bar = ServiceRegistry.get(BarManager.__name__)
bar.LoadContent()