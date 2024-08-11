import game

key = game.Environments.ATARI

folder: str = game.Folders[key]
print(folder)

file: str = f"{folder}/files.txt"
with open(file, 'rt') as fh:
    lines = fh.readlines()
    for line in lines:
        print(line.strip())