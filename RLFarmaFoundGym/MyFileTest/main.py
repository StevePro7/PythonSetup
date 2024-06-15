
def printer() -> str:
    text: str = None
    with open('gamefile.txt', 'r') as file:
        for line in file:
            text = line.strip()
            if not text.startswith('#'):
                break

    return text



if __name__ == '__main__':
    text: str = printer()
    print(text)
