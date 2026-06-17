from Managers.ConfigManager import ConfigManager
from Managers.BaseManager import BaseManager
from Engine.Bootstrap import build_game


registry = build_game()

baseManager = registry.get(BaseManager.__name__)
baseManager.Initialize()

configManager = registry.get(ConfigManager.__name__)
configManager.Initialize()
configManager.LoadContent()
configManager.DumpConfig()
