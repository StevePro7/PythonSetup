# 2. Thread Creation
import threading

def process():
    pass

thread = threading.Thread(target=process)
thread.start()
thread.join()
