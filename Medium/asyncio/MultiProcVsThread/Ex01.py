import threading
import time

def download_data():
    time.sleep(2)  # Simulate network delay
    print("Data downloaded")

threads = [threading.Thread(target=download_data) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()