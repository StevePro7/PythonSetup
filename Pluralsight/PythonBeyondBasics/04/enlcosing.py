#enclosing
message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing msg1', message)
    local()
    print('enclosing msg2', message)

if __name__ == '__main__':
    print('beg')
    print('global msg1', message)
    enclosing()
    print('global msg2', message)
    print('end')
