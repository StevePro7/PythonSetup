import threading
import time

def square_numbers():
    for i in range(10000000):
        _ = i * i

threads = [threading.Thread(target=square_numbers) for _ in range(4)]
start_time = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Threading time taken:", time.time() - start_time)