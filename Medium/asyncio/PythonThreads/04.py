# Tow threads in the foreground
import threading

def countSeconds():
    print("Second")
    #threading.Timer(1, countSeconds, daemon=True).start()
    threading.Timer(1, countSeconds).start()

def countTenSeconds():
    print("Ten seconds passed")
    threading.Timer(10, countTenSeconds).start()

threading.Timer(1, countSeconds).start()
threading.Timer(10, countTenSeconds).start()