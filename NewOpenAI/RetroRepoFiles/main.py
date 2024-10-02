import file
import func
import game

key = game.Environments.SMS
#key = game.Environments.GENESIS


if __name__ == '__main__':
    folder: str = game.Folders[key]
    path: str = f"{folder}/files.txt"
    lines: list = file.init(path)
    name: str = file.load(lines)
    if len(name) > 0:
        func.run_game(name)
    print("The end")