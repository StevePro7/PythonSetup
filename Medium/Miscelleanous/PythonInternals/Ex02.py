import threading

def count():
    x = 0
    for _ in range(10**7):
        x += 1

threads = [threading.Thread(target=count) for _ in range(4)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]