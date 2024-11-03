import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i} beg")
        time.sleep(i)
        print(f"Thread 1: {i} end")

def print_letters():
    for letter in "abcde":
        print(f"Thread 2: {letter} beg")
        time.sleep(1)
        print(f"Thread 2: {letter} end")

# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")