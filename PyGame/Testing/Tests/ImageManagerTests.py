from Managers.ImageManager import ImageManager
from Managers.RandomManager import RandomManager
from bootstrap import build_game



registry = build_game()

imageManager = registry.get(ImageManager.__name__)
randomManager = registry.get(RandomManager.__name__)

imageManager.Initialize()
randomManager.Initialize()

imageManager.LoadContent()
imageManager.GenerateNextActor()
