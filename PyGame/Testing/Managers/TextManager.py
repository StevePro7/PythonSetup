from MyGame import MyGame
from Objects.TextData import TextData
from Static.Assets import Assets
from Static.Colors import Colors
from utils import get_project_root
from pathlib import Path


class TextManager:
    def __init__(self):
        self.DELIM = ","

    def Initialize(self):
        pass

    def LoadTextData(self, screen: str) -> list[TextData]:
        file: str = self.GetTextFile(f"{screen}.txt")
        lines: list[str] = MyGame.Manager.FileManager.LoadTxt(file)

        textDataList: list[TextData] = []
        for line in lines:
            if line.startswith("##") or line.startswith("--"):
                continue

            items = line.split(self.DELIM)
            x = int(items[0])
            y = int(items[1])
            text = items[2]

            position: tuple[int, int] = self.GetTextPosition(x, y)
            textData: TextData = TextData(position, text, Colors.White)
            textDataList.append(textData)

        return textDataList


    def Update(self, deltaTime: int):
        pass

    def DrawText(self, text, position, color=Colors.White):
        MyGame.Manager.GraphicsManager.DrawText(Assets.EmulogicFont, text, position, color)

    def DrawTextDataList(self, textDataList: list[TextData]) -> None:
        for textData in textDataList:
            self.DrawText(textData.Text, textData.Position, textData.Color)

    def GetTextFile(self, textFile: str) -> str:
        root: Path = get_project_root()
        file: Path = root / "Data" / textFile
        return file

    def GetTextPosition(self, x: int, y: int) -> tuple[int, int]:
        font_size: int = 20 # MyGame.Manager.FontManager.FontSize
        position: tuple[int, int] = (x * font_size, y * font_size)
        return position