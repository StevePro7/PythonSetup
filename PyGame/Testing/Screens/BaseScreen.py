from abc import ABC, abstractmethod
from enumerations import ScreenType
from Objects.TextData import TextData
from MyGame import MyGame


class BaseScreen(ABC):

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


    # def LoadTextData(self, screen: str):
    #     self.textDataList: list[TextData] = MyGame.Manager.TextManager.LoadTextData(screen)