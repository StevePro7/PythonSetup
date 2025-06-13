def outer():
    x = 'enclosing'
    def inner():
        print(x)        # Resolved from enclosing scope
    inner()


outer()