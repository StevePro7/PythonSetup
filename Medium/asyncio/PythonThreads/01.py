import threading

def hello_world():
    print("Hello, world!")

t = threading.Thread(target=hello_world)
t.start()