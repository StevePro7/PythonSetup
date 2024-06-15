
def get_content():
    with open('transcript.txt', 'r') as file:
        content = file.read()

    return content



if __name__ == '__main__':
    count = 1
    list = []
    content = get_content()
    lines = content.splitlines()
    for line in lines:
        if len(line.strip()) == 0:
            with open('example.txt', 'a') as file:
                for l in list:
                    file.write(l)
                    file.write('\n')
                list = []
        else:
            list.append(line)
        print(line)
