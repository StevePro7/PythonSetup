dirX: str = "Atari"

def get_lines(dirX: str) -> list:
    file: str = f"{dirX}/files.txt"
    with open(file, 'r') as fh:
        lines = fh.readlines()
    return lines



if __name__ == '__main__':
    lines: list = get_lines(dirX)

    listA: list = []
    listB: list = []
    listC: list = []
    listD: list = []

    i = 0
    for line in lines:
        line = line.strip()
        if 0 == i:
            listA.append(line)
        if 1 == i:
            listB.append(line)
        if 2 == i:
            listC.append(line)
        if 3 == i:
            listD.append(line)
        i += 1

        if 4 == i:
            i = 0
        print(line)
