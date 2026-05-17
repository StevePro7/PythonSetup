from generate_stubs import MyGame

from BarManager import BarManager
from FooManager import FooManager
from GameManager import GameManager
barmanager = BarManager()
foomanager = FooManager()

manager: GameManager = GameManager(barmanager, foomanager)
MyGame.Construct(manager)
MyGame.Initialize()
MyGame.LoadContent()
