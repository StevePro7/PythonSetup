from help import Environments
from help import Folders

key: int = Environments.ATARI.value

folder: str = Folders[key]
print(folder)

file: str = f"{folder}/files.txt"
with open(file, 'rt') as fh:
    lines = fh.readlines()
    for line in lines:
        print(line.strip())