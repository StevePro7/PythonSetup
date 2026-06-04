from Managers.ConfigManager import ConfigManager
from bootstrap import build_game

registry = build_game()

configManager = registry.get(ConfigManager.__name__)
configManager.LoadContent()
configManager.DumpConfig()
