from pathlib import Path
from MyGame import MyGame
from Objects.TextData import TextData
from Static.Assets import Assets
from Static.Colors import Colors
from Static import Constants as const


class TextManager:
    def __init__(self):
        self.contentRoot: Path = None
        self.textsRoot: Path = None
        self.DELIM = ","

    def Initialize(self):
        self.contentRoot = MyGame.Manager.BaseManager.GetContentRoot()
        self.textsRoot = self.contentRoot / const.DATA_DIRECTORY / const.TEXTS_DIRECTORY
        self.color = Colors.Black


    def InitTextData(self, screen: str) -> list[TextData]:
        file: str = self.__getTextFile(f"{screen}.txt")
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
            textData: TextData = TextData(position, text, Colors.Black)
            textDataList.append(textData)

        return textDataList


    def GetTextPosition(self, x: int, y: int) -> tuple[int, int]:
        px = x * const.FONT_SIZE + const.FontOffsetX
        py = y * const.FONT_SIZE + const.FontOffsetY
        position: tuple[int, int] = (px, py)
        return position


    def GetWhitePosition(self, x: int, y: int) -> tuple[int, int]:
        px = x * const.FONT_SIZE + const.GameOffsetX
        py = y * const.FONT_SIZE
        position: tuple[int, int] = (px, py)
        return position


    def DrawText(self, text: str, x: int, y: int):
        position: tuple[int, int] = self.GetTextPosition(x, y)
        self.DrawTextPos(text, position)

    def DrawTextPos(self, text: str, position: tuple[int, int], color: Colors = Colors.Black):
        MyGame.Manager.GraphicsManager.DrawText(Assets.EmulogicFont, text, position, color)

    def DrawTextDataList(self, textDataList: list[TextData]) -> None:
        for textData in textDataList:
            self.DrawTextPos(textData.Text, textData.Position, textData.Color)


    def __getTextFile(self, textFile: str) -> str:
        file: Path = self.textsRoot / textFile
        return file