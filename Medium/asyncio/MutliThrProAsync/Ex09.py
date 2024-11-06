# 09. - Lock
import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    with lock:
        for _ in range(1000):
            counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(counter)  # Should be 10000