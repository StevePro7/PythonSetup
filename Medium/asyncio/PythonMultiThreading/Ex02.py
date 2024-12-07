# 3. Thread Synchronization
import threading

lock = threading.Lock()

def lock_section():
    with lock:
        # Critical code goes here
        print("This is thread-safe section")
