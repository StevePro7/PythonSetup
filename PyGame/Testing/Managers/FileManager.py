class FileManager:


    def LoadTxt(self, file: str) -> list[str]:
        lines: list[str] = []

        with open(file, "r", encoding="utf-8") as reader:
            line = reader.readline()

            while line:
                lines.append(line.rstrip("\n"))
                line = reader.readline()

        return lines
