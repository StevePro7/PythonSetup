from abc import ABC, abstractmethod
from enumerations import ScreenType

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
