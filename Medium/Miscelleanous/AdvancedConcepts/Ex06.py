import threading

def task():
    print("Task executed")

thread = threading.Thread(target=task)
thread.start()
thread.join()