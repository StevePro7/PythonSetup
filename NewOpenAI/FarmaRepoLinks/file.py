# TODO - read file contents


def init(path: str) -> list:
    with open(path, 'rt') as file_handle:
        return file_handle.readlines()

    #     for line in lines:
    #         print(line.strip())
    #
    # return ['BipedalWalker-v3\n', 'CarRacing-v2\n', '#LunarLander-v2']


def load(lines: list) -> str:
    name: str = ""

    for line in lines:
        line = line.strip()
        if not str.startswith(line, '#'):
            name = line
            break

    return name
