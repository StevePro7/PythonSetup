
def get_content():
    with open('transcript.txt', 'r') as file:
        content = file.read()

    return content



if __name__ == '__main__':
    valu = 1
    list = []
    content = get_content()
    lines = content.splitlines()
    for line in lines:
        if len(line.strip()) == 0:
            name: str = str(valu).zfill(2)
            with open(f'files/{name}.txt', 'a') as file:
                for l in list:
                    file.write(l)
                    file.write('\n')
                list = []
                valu += 1
        else:
            list.append(line)

    if len(list) > 0:
        name: str = str(valu).zfill(2)
        with open(f'files/{name}.txt', 'a') as file:
            for l in list:
                file.write(l)
                file.write('\n')
