from abc import ABC, abstractmethod
from enumerations import ScreenType
from Objects.TextData import TextData
from MyGame import MyGame


class BaseScreen(ABC):

    def __init__(self):
        self.textDataList: list[TextData] = []


    @abstractmethod
    def Initialize(self) -> None:
        pass

    @abstractmethod
    def LoadContent(self) -> None:
        pass

    @abstractmethod
    def Update(self, deltaTime: int) -> ScreenType | None:
        return None

    @abstractmethod
    def Draw(self) -> None:
        pass


    def LoadScreenText(self) -> None:
        screen_name = self.__class__.__name__
        self.textDataList = MyGame.Manager.TextManager.LoadTextData(screen_name)

    def DrawScreenText(self) -> None:
        MyGame.Manager.TextManager.DrawTextDataList(self.textDataList)