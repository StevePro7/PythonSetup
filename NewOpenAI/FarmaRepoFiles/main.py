
def get_lines(dirX: str) -> list:
    file: str = f"{dirX}/files.txt"
    with open(file, 'r') as fh:
        lines = fh.readlines()
    return lines


def put_file(dirX, name: str):
    text = name.replace('"', '')
    text = text.replace(' ', '')
    text = text.replace('name=', '')
    file: str = f"{dirX}/{text}.py"
    with open(file, 'w') as fh:
        fh.write("from func import run_game\n")
        fh.write("\n")
        fh.writelines(f"run_game({name})\n")

if __name__ == '__main__':
    dirX: str = "Box2D"
    lines: list = get_lines(dirX)
    for line in lines:
        line = line.strip()
        #print(line)

    put_file(dirX, 'name = "BipedalWalker-v3"')
    print(lines)


