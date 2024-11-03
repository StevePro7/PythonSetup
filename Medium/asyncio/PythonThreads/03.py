# Using lists
import concurrent.futures
import threading

threads = list()

def thread_function(index):
    pass

for index in range(3):
    print(f"Main    : create and start thread '{index}.")
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    print(f"Main    : before joining thread '{index}'", index)
    thread.join()
    print(f"Main    : thread '{index}' done", index)

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))