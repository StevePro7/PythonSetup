# 02. - Multithreading
import threading
import time

def background_task():
    while True:
        print("Running background task")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task, daemon=True)

# Start the thread
thread.start()

# Main program continues
time.sleep(5)
print("Main program exits")