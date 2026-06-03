import pygame
from Managers.ImageManager import ImageManager
from bootstrap import build_game



registry = build_game()

pygame.init()
imageManager = registry.get(ImageManager.__name__)
imageManager.Initialize()
imageManager.LoadContent()
print("bye")