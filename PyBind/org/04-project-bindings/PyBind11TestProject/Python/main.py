import myproject

def print_hi(name):
    msg1: str = f'Hi, {name}'
    msg2: str = myproject.greet("adriana")

    print(msg1)
    print(msg2)

if __name__ == '__main__':
    print_hi('stevepro')
