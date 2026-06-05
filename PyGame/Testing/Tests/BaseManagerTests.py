from Managers.BaseManager import BaseManager
from bootstrap import build_game
import pygame

registry = build_game()

baseManager = registry.get(BaseManager.__name__)


#baseManager.GetPositionsSelect()
#pos: pygame.Vector2 = baseManager.GetPositionSelect(0, 0)
#print(pos)

#vec = baseManager.GetLeftArrowPos()
#vec = baseManager.GetRghtArrowPos()
vec = baseManager.GetVolumeIconPos()
print(vec)