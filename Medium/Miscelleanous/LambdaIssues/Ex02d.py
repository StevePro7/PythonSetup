def make_callback(value):
    def callback():
        return value
    return callback

funcs = [make_callback(i) for i in range(5)]