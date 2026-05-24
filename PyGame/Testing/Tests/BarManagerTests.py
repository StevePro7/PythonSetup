from Managers.BarManager import BarManager
from bootstrap import build_game

registry = build_game()

bar = registry.get(BarManager.__name__)
bar.LoadContent()

tv = bar.TestValue()
assert 12 == tv
