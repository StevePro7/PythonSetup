from Managers.ImageManager import ImageManager
from bootstrap import build_game



registry = build_game()

imageManager = registry.get(ImageManager.__name__)
imageManager.Initialize()
imageManager.LoadContent()
