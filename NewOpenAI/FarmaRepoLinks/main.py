import file
import func
import game

#key = game.Environments.ATARI
key = game.Environments.TOY_TEXT


if __name__ == '__main__':
    folder: str = game.Folders[key.value]
    path: str = f"{folder}/files.txt"
    lines: list = file.init(path)
    name: str = file.load(lines)
    func.run_game(name)
